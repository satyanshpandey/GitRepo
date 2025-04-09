
from django.contrib.auth.models import User


from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
    def create(self, validated_data):
        if 'name' in validated_data:
            validated_data['name'] = "Prefix_added_by_satyansh____" +validated_data['name']
        isinstance = Employee.objects.create(**validated_data)
        return isinstance
        # return super().create(validated_data)
        
class userSerializersModelData(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"