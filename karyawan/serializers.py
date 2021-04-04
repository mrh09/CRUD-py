from karyawan.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class meta:
        model = Employee
        fields = ['id', 'name', 'position', 'division']