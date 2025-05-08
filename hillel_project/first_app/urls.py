from django.urls import path

from first_app.views import func_views, generic_views

urlpatterns = [
    # path('employees/', func_views.employee_list, name='employee_list'),
    path('employees/', generic_views.EmployeeListView.as_view(), name='employee_list'),
    # path('employees/update/<int:pk>/', func_views.employee_update, name='employee_update'),
    path('employees/update/<int:pk>/', generic_views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', func_views.employee_delete, name='employee_delete'),
    path('querysets/', func_views.queryset_route, name='querysets'),
    path('salary-calculator/', generic_views.SalaryCalculatorView.as_view(), name="salary_calc")

]