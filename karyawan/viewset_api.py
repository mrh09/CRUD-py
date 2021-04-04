from karyawan.models import Employee
from karyawan.serializers import EmployeeSerializer
from rest_framework import viewsets, permissions

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]