from rest_framework import generics
from ...models import Classroom
from ...serializers import ClassroomSerializer

class ClassroomListCreate(generics.ListCreateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class ClassroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
