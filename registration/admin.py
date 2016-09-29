from django.contrib import admin
from .models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    
    list_display = ['first_name', 'last_name', 'email', 'gender', 'school', 'course', 'registered_timestamp', 'Student_Enrollment_Class', 'student_photo']
    list_filter = ['year', 'registered_timestamp']
    search_fields = ['first_name', 'last_name', 'year', 'Student_Enrollment_Class']
    
    class Meta:
        model = Student

admin.site.register(Student, StudentAdmin)

