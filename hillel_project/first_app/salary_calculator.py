import logging
import math
from abc import ABC, abstractmethod
import datetime

from first_app.models import Employee, MonthlySalary
from common.enums import WorkDayEnum

logger = logging.getLogger("default")

class AbstractSalaryCalculator(ABC):
    sick_days_multiplier = 0.6

    def __init__(self, employee: Employee):
        self.employee = employee


    @abstractmethod
    def calculate_salary(self, days_dict: dict[str, int]):
        raise NotImplementedError()


class CalculateMonthRateSalary(AbstractSalaryCalculator):

    def __init__(self, employee: Employee):
        super().__init__(employee)
        self._daily_payment = 0

    @staticmethod
    def _calculate_base_work_days(days_dict):
        return len(
            {
                day: work_type
                for day, work_type in days_dict.items()
                if work_type not in (WorkDayEnum.WEEKEND.name, WorkDayEnum.HOLIDAY.name)
            }
        )

    def _get_daily_salary(self, base_working_days: int) -> int:
        return math.ceil(self.employee.position.monthly_rate/base_working_days)

    def _get_work_days_payment(self, days_dict):
        work_days = len({day: day_type for day, day_type in days_dict.items() if day_type == WorkDayEnum.WORKING_DAY.name})
        return work_days * self._daily_payment

    def _get_sick_days_payment(self, days_dict):
        sick_days = len({day: day_type for day, day_type in days_dict.items() if day_type == WorkDayEnum.SICK_DAY.name})
        return sick_days * math.ceil(self._daily_payment * self.sick_days_multiplier)


    def calculate_salary(self, days_dict: dict[str, int]):
        base_days = self._calculate_base_work_days(days_dict) #for addit.check.division by zero protection for working days

        if base_days == 0:                                                      #same
            raise ValueError("Неможливо розрахувати зарплату без робочих днів") #same

        self._daily_payment = self._get_daily_salary(base_working_days=self._calculate_base_work_days(days_dict))

        work_days_payment = self._get_work_days_payment(days_dict)
        sick_days_payment = self._get_sick_days_payment(days_dict)

        salary = work_days_payment + sick_days_payment
        return salary if salary <= self.employee.position.monthly_rate else self.employee.position.monthly_rate


    def save_salary(self, salary: int, date: datetime.date):
        start_month_date = date.replace(day=1)

        if MonthlySalary.objects.filter(date=start_month_date, employee=self.employee).exists():
             logger.warning(f"Salary for Employee {self.employee} for {start_month_date.month}/{start_month_date.year} already paid!")
        else:
            MonthlySalary.objects.update_or_create(
                date=start_month_date,
                salary=salary,
                employee=self.employee,
                is_paid=True
            )

