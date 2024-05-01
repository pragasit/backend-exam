from rest_framework import generics
from ...models import Student
from ...serializers import StudentSerializer
from ...filters import StudentFilter

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
