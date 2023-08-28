from . import views
from django.urls import path

urlpatterns =[
    path('',views.home),
    path('fun_employee_details/', views.fun_employee_details),
    path('employee_details_class/<int:pk>/', views.employee_details_class.as_view()),
    path('employee_list/', views.employee_list.as_view(), name='employee_list'),
]