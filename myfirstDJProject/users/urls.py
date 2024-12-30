from django.urls import path
from .views import home,user_login,employee_form

urlpatterns = [
    path('', user_login, name='login'),
    path('employee_form/', employee_form, name='employee_form'),
    #path('', home, name='home'),  # Add a route for the root URL
]