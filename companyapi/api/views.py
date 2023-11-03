from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee
from .serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{companies_id}/Employee
    @action(detail=True, methods=['get'])
    def employee(self, request, pk = None):
        try:
            comp = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=comp)
            emp_ser = EmployeeSerializer(emps, many=True, context={"request": request})
            return Response(emp_ser.data)
        except Exception as e:
            print(e)
            return ResourceWarning({'message': e})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer