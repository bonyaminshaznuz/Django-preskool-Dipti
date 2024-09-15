from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from myadminapp.forms import *
from myadminapp.models import * 
from django.contrib import messages
from django.contrib.auth import get_user_model
#from myadminapp.tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from myadminapp.middlewares import auth, guest
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .decorators import role_required

@auth
@role_required('admin', 'student', 'teacher')
def profile(request):
    return render(request, 'adminApp/profile.html')


@guest
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=True
            user.user_type = 'student'
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'adminApp/register.html', {'form': form})

@guest
def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'adminApp/login.html', {'form': form})

@auth
def logout_page(request):
    logout(request)
    return redirect('login')


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'adminApp/forgot-password.html'
    email_template_name = 'adminapp/password_reset_email.html'
    subject_template_name = 'adminapp/password_reset_subject.txt'
    success_url = reverse_lazy('login')


@auth
def editadminpage(request, id):
    user = Custom_User.objects.get(id=id)
    return render(request, 'adminApp/edit-admin-page.html', {'Custom_User': user})

@auth
def updateadminpage(request, id):
    user = Custom_User.objects.get(id=id)
    if request.method == 'POST':
        form = editadminprofile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = editadminprofile(instance=user)

    return render(request, 'adminApp/edit-admin-page.html', {'form': form, 'user': user})

@auth
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'adminApp/profile.html', {'form': form})

@auth
def subjects(request):
      subjects = Subject.objects.all()  
      return render(request, 'adminApp/subjects.html',{'subjects':subjects})

@auth
def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm() 
    
    return render(request, 'adminApp/add-subject.html', {'form': form})

@auth
def edit_subject(request, id):
    subjects = Subject.objects.get(id=id)
    return render(request, 'adminApp/edit-subject.html', {'Subject': subjects})

@auth
def update_subject(request, id):
    sub = Subject.objects.get(id=id)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=sub)
        if form.is_valid():
            form.save()
            return redirect('subjects')
    else:
        form = SubjectForm(instance=sub)

    return render(request, 'adminApp/edit-subject.html', {'form': form, 'sub': sub})

@auth
def destroy_sub(request, id):  
    sub = Subject.objects.get(id=id)  
    sub.delete()  
    return redirect('subjects')

@auth
def indexpage(request):
    return render(request,'adminApp/index.html')

def depertment_views(request):
    departments = Department.objects.all()  
    return render(request, 'adminApp/departments.html',{'departments':departments})


def add_depertment(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depertments')
    else:
        form = DepartmentForm() 
    
    return render(request, 'adminApp/add-department.html', {'form': form})


def edit_department(request, id):
    department = Department.objects.get(id=id)
    return render(request, 'adminApp/edit-department.html', {'Department': department})


def update_department(request, id):
    dept = Department.objects.get(id=id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            return redirect('depertments')
    else:
        form = DepartmentForm(instance=dept)

    return render(request, 'adminApp/edit-department.html', {'form': form, 'dept': dept})

def destroy_dept(request, id):  
    sub = Department.objects.get(id=id)  
    sub.delete()  
    return redirect('depertments')


def student_view(request):
    my_user = Custom_User.objects.filter(user_type='student').select_related('department')
    return render(request, 'adminApp/students.html',{'my_user':my_user})


def edit_student_view(request, id):
    students = Custom_User.objects.get(id=id)
    return render(request, 'adminApp/edit-student.html', {'students': students})


def teacher_view(request):
    my_user = Custom_User.objects.filter(user_type='teacher').select_related('subject')
    return render(request, 'adminApp/teachers.html',{'my_user':my_user})

def edit_teacher_view(request, id):
    myuser= Custom_User.objects.get(id=id)
    return render(request, 'adminApp/edit-teacher.html',{'myuser':myuser})


def updateteacherspage(request, id):
    myuser = Custom_User.objects.get(id=id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=myuser)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    else:
        form = TeacherForm(instance=myuser)

    return render(request, 'adminApp/edit-teacher.html', {'form': form, 'myuser': myuser})