from django.urls import path
from django.views.decorators.cache import cache_page

from first_app.views import func_views, generic_views

urlpatterns = [
    # path('employees/', func_views.employee_list, name='employee_list'),
    path('employees/', cache_page(60)(generic_views.EmployeeListView.as_view()), name='employee_list'),
    path('employees/<int:pk>/', generic_views.EmployeeDetailsView.as_view(), name='employee_details'),
    path('employees/update/<int:pk>/', generic_views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', func_views.employee_delete, name='employee_delete'),
    path('employees/create/', generic_views.EmployeeCreateView.as_view(), name='employee_create'),
    path('querysets/', func_views.queryset_route, name='querysets'),
    path('salary-calculator/', generic_views.SalaryCalculatorView.as_view(), name="salary_calc")

]