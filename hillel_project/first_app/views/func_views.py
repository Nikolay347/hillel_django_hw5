from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from first_app.models import Employee
from first_app.forms import EmployeeForm
from first_app.utils import is_user_superuser
from first_app.querysets import examples


@user_passes_test(is_user_superuser)
def employee_list(request):
    employees = Employee.objects.all()
    search = request.GET.get("search", '')
    if search:
        employees = Employee.objects.filter(
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(position__title__icontains=search)
        )
    context = {
        "employees": employees
    }
    return render(request, "employee_list.html", context=context)


@user_passes_test(is_user_superuser)
def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(reverse('employee_list'))
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

@user_passes_test(is_user_superuser)
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect(reverse('employee_list'))
    return render(request, 'employee_confirm_delete.html', {'object': employee})




def queryset_route(request):
    examples()
    return HttpResponse()