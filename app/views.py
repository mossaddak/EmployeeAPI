from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Employee
from .serializer import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework import status
from django.urls import reverse

@api_view(['POST'])
#@csrf_exempt 
def employeeListView(request):
    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
            return redirect("/api/")
        else:
            print("____________________________________________________________________________________________")
            print(serializer.errors)


def employeeyApi(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)

def InsertAndInfo(request):
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        #file = request.FILES['filedf'] if 'filedf' in request.FILES else None
        
        data = {
            'name':name,     
            'email':email,
            'phone':phone,
            #'img':file
        }
        print("_______________________________________________________________________________________________________________________________")
        print(data)
        headers = {'Content-Type' : 'application/json'}

        status_url = request.build_absolute_uri(reverse('employeeListView'))

        requests.post(status_url,json=data,headers=headers)
        return redirect("/api/")

        


    employeeInfoApiLink = requests.get('http://127.0.0.1:8000/api/employeeyApi/').json()
    context = {
        "employeeInfo":employeeInfoApiLink
    }
    return render(request, 'InsertAndInfo.html',context)

# {
#     "name":"kamrul",
#     "email":"kamrul@gmail.com",
#     "phone":"554877"
# }
