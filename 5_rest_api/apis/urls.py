from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1.school import SchoolListCreate, SchoolDetail
from .views.v1.classroom import ClassroomListCreate, ClassroomDetail
from .views.v1.teacher import TeacherListCreate, TeacherDetail
from .views.v1.student import StudentListCreate, StudentDetail


router = DefaultRouter()

api_v1_urls = (router.urls, 'v1')

urlpatterns = [
    path('v1/', include(api_v1_urls)),
    path('schools/', SchoolListCreate.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', SchoolDetail.as_view(), name='school-detail'),
    path('classrooms/', ClassroomListCreate.as_view(), name='classroom-list-create'),
    path('classrooms/<int:pk>/', ClassroomDetail.as_view(), name='classroom-detail'),
    path('teachers/', TeacherListCreate.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
]
