from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_User(AbstractUser):
    user_type = [
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ]   
    user_type = models.CharField(choices=user_type, max_length=20)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="Media/Profile_pic", blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    mobile_number = models.CharField(max_length=120, unique=True, null=True, blank=True)
    user_description = models.CharField(max_length=120, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s')
    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s')


    def __str__(self):
        return self.full_name


class Department(models.Model):
    department_id = models.CharField(max_length=100, null=True, blank=True)
    department_name = models.CharField(max_length=255, null=True, blank=True)
    head_of_department = models.ForeignKey(Custom_User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'}, related_name='Department', null=True, blank=True)
    department_start_date = models.DateField()
    no_of_students = models.PositiveIntegerField()

    def __str__(self):
        return self.department_name


class Subject(models.Model):
    sub_name = models.CharField(max_length=100, null=True, blank=True)
    sub_code = models.CharField(max_length=100, null=True, blank=True)
    class_name = models.CharField(max_length=50, null=True, blank=True)
    teacher = models.ForeignKey(Custom_User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'teacher'}, related_name='subjects', null=True, blank=True)

    def __str__(self):
        return self.sub_name

