from rest_framework import serializers
from mySchoolApp.models.student import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        abstract = True
        fields = '__all__'
        # exclude = ('id')
