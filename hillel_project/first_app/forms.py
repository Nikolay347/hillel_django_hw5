from datetime import date
import calendar
from django import forms
from django.forms import ChoiceField

from first_app.models import Employee

from common.enums import WorkDayEnum


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('username', 'first_name', 'last_name', 'email', 'position')




class SalaryForm(forms.Form):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        error_messages={
            'required': 'Потрібно обрати працівника.'
        }
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = date.today()


        week_day, num_days = calendar.monthrange(today.year, today.month)
        for day in range(1, num_days + 1):
            day_coord = today.year, today.month, day

            weekday = calendar.weekday(*day_coord)
            weekday_name = calendar.day_name[weekday]
            field_name = f"day_{day}"

            if calendar.weekday(*day_coord) >= 5:
                self.fields[field_name] = ChoiceField(
                    label=f'{day} - {weekday_name}',
                    choices=[(WorkDayEnum.WEEKEND.name, WorkDayEnum.WEEKEND.value)], # [("WEEKDAY", "working_day")]
                    initial=WorkDayEnum.WEEKEND.name
                )

            else:
                self.fields[field_name] = ChoiceField(
                    label=f'{day} - {weekday_name}',
                    choices=[(option.name, option.value) for option in WorkDayEnum],
                    initial=WorkDayEnum.WORKING_DAY.name,
                )

# Adding sick, holiday and employee validation checks(validation = message if the user has not selected an employee
# or if sick days > 5, or if holiday days > 3)
    def clean_employee(self):
        employee = self.cleaned_data.get('employee')
        if not employee:
            raise forms.ValidationError("Потрібно обрати працівника.")
        return employee

    def clean(self):
        cleaned_data = super().clean()
        sick_days_count = 0
        holiday_days_count = 0

        for key, value in cleaned_data.items():
            if key.startswith("day_") and value == WorkDayEnum.SICK_DAY.name:
                sick_days_count += 1
            if key.startswith("day_") and value == WorkDayEnum.HOLIDAY.name:
                holiday_days_count += 1

        if sick_days_count > 5:
            raise forms.ValidationError(f"Кількість лікарняних днів не може перевищувати 5. Зараз: {sick_days_count}")
        if holiday_days_count > 3:
            raise forms.ValidationError(f"Кількість святкових днів не може перевищувати 3. Зараз: {holiday_days_count}")

        return cleaned_data