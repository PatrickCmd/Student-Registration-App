from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404

# django modalforms
# from django_modalview.generic.edit import ModalCreateView, ModalUpdateView, ModalDeleteView
# from django_modalview.generic.component import ModalResponse
from code import code
from .models import Student
from .forms import StudentForm

# Creating new student object using Modalforms

# class StudentCreate(ModalCreateView):
#     
#     def __init__(self, *args, **kwargs):
#         super(StudentCreate, self).__init__(*args, **kwargs)
#         self.title = 'Add New Student'
#         self.description = 'Student Registration'
#         self.form_class = StudentForm
#     
#     def form_valid(self, form, **kwargs):
#         self.response = ModalResponse("Student created", "Success")
#         return super(StudentCreate, self).form_valid(form, **kwargs)

# listing all students

def StudentCreate(request):
    
    form = StudentForm(request.POST or None, request.FILES or None)
    message = None
    
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get('first_name'))
        print(form.cleaned_data.get('last_name'))
        instance = form.save()
        message = 'Student successfully registered'
        form = None
    
    context = {
        'title': 'Student Registration',
        'message': message,
        'form': form
    }
    
    return render(request, 'students/createStudent.html', context)

def Student_list(request):
    student_list = Student.objects.all()     # queryset for selecting all students using model  manager
    context = {
        'heading': 'Students List',
        'students': student_list,
    }
    return render(request, 'students/student_list.html', context)


def StudentEdit(request, pk=None):
    instance = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, request.FILES or None, instance=instance)
    message = None
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("last_name"))
        instance.save()        
        messages.success(request, 'Student successfully updated')
        message = 'Student successfully updated'
        form = None
        # return HttpResponseRedirect(instance.get_absolute_url())
    
    context = {
        'title': 'Edit Student',
        'instance': instance,
        'message': message,
        'form': form
    }
    
    return render(request, 'students/editStudent.html', context)

def StudentDetail(request, pk=None):
    instance = get_object_or_404(Student, pk=pk)
    
    context = {
        'title': 'Student Details',
        'instance': instance
    }
    
    return render(request, 'students/detailStudent.html', context)

def StudentDelete(request, pk=None):
    instance = get_object_or_404(Student, pk=pk)
    instance.delete()
    messages.success(request, 'Student successfully deleted')
    return redirect('students:list')
        
    