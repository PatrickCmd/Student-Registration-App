#!/usr/bin/env python
from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'gender',
            'Student_Enrollment_Class',
            'school',
            'course',
            'student_photo',
        ]
