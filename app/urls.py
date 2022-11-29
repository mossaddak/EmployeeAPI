from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('employees/', views.employeeListView, name="employeeListView"),
    path('employeeyApi/', views.employeeyApi, name="employeeyApi"),
    path('', views.InsertAndInfo, name="InsertAndInfo"),
]
