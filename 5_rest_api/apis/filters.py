from django_filters import FilterSet, filters
import django_filters
from .models import School, Teacher, Student

class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class TeacherFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender']

class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender']


# code here
