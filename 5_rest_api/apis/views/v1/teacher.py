from rest_framework import generics
from ...models import Teacher
from ...serializers import TeacherSerializer
from ...filters import TeacherFilter

class TeacherListCreate(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filterset_class = TeacherFilter

class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
