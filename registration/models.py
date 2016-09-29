from __future__ import unicode_literals
from django.core.urlresolvers import reverse

from django.db import models

# student model Manager.

class StudentManager(models.Manager):
    
    def all(self):
        qs = super(StudentManager, self).order_by('registered_timestamp')      # getting all students ordering by timestamp
        return qs


def upload_location(instance, filename):
    return ("%s/%s" % (instance, filename))


class Student(models.Model):
    
    SCHOOL_CHOICES = (
        ('FR', 'Fresher'),
        ('CONT', 'Continuing'),
        ('GRAD', 'Graduating')
    )
    
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    
    DEPARTMENT = (
        ('SBA', 'School of Business Administration'),
        ('SCIAD', 'School of Industry Art and Design'),
        ('SLAW',  'School of Law'),
        ('SCOS', 'School of Social Sciences'),
        ('SHES', "School of Humanities Education and Social Development")
    )
    
    COURSES = (
        ('BIT', "Bachelor of Information Technology"),
        ('BCS', "Bachelor of Computer Science"),
        ('BPLM', 'Bachelor of Procument and Logistics Management'),
        ('BES', 'Bachelor of Education Social Development')
    )
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER)
    registered_timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    year = models.DateField(auto_now=False, auto_now_add=True)
    Student_Enrollment_Class = models.CharField(max_length=4, choices=SCHOOL_CHOICES)
    school = models.CharField(max_length=255, choices=DEPARTMENT)
    course = models.CharField(max_length=255, choices=COURSES                          )
    student_photo = models.ImageField(
                                        upload_to = upload_location,
                                        null = True, blank=True,
                                        width_field = 'width_field',
                                        height_field = 'height_field',
                                    )
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    
    
    objects = StudentManager()     # intiating the model Manager
    
    
    def __str__(self):
        return self.first_name + '-' + self.last_name
    
    def __unicode__(self):
        return self.first_name + '-' + self.last_name
    
    def get_absolute_url(self):
        return reverse('students:student_detail', kwargs={'pk': self.pk})
    
    def get_edit_url(self):
        return reverse('students:student_update', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('students:student_delete', kwargs={'pk': self.pk})
    