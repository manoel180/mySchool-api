from mySchoolApp.serializers import CourseSerializer

from rest_framework import permissions, viewsets

from mySchoolApp.models.course import Course


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all().order_by('name')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]