from rest_framework import generics
from ...models import School
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter

class SchoolListCreate(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filterset_class = SchoolFilter

class SchoolDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
