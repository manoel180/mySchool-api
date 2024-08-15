from rest_framework import serializers

from mySchoolApp.models.course import Course


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        abstract = True
        fields = '__all__'
        # exclude = ('id')
