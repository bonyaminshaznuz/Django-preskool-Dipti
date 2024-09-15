from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from myadminapp.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ['username', 'email', 'password1', 'password2']
        
        
        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Custom_User  
        fields = ['username', 'password']


class editadminprofile(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['full_name', 'email', 'city', 'profile_image', 'dob', 'mobile_number', 'user_description']  

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['sub_code','sub_name', 'class_name'] 

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_id','department_name','head_of_department','department_start_date', 'no_of_students']   

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Custom_User
        fields = ['full_name', 'email', 'city', 'dob', 'mobile_number']  