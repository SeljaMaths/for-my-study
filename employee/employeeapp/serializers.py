from . models import *
from rest_framework import serializers


class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model =employee_details
        fields ='__all__'