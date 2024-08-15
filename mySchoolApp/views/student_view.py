from rest_framework import permissions, viewsets

from mySchoolApp.models.student import Student
from mySchoolApp.serializers.student_serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Student.objects.all().order_by('name')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]