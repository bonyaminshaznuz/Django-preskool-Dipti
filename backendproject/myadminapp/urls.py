from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import ResetPasswordView

urlpatterns = [ 
    path('', views.indexpage,name='indexpage'),  
    path('login/', views.loginPage,name='login'), 
    path('profile/', views.profile,name='profile'), 
    path('register/', views.register,name='register'), 
    path('logout/',views.logout_page, name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='adminApp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='adminApp/login.html'), name='password_reset_complete'),
    path('edit/<int:id>', views.editadminpage,name='editadminpage'),
    path('updateadminpage/<int:id>', views.updateadminpage,name='updateadminpage'),
    path('change_password/<int:id>', views.change_password, name='change_password'),
    path('subjects/', views.subjects, name='subjects'),
    path('add-subject/', views.add_subject, name='add-subject'),
    path('edit-subject/<int:id>', views.edit_subject, name='edit-subject'),
    path('update-subject/<int:id>', views.update_subject, name='update_subject'),
    path('delete-subject/<int:id>', views.destroy_sub,name='destroy_sub'), 
    path('depertments/', views.depertment_views, name='depertments'),
    path('add-depertment/', views.add_depertment, name='add-depertment'),
    path('edit-department/<int:id>', views.edit_department, name='edit-department'),
    path('update-department/<int:id>', views.update_department, name='update_department'),
    path('delete-department/<int:id>', views.destroy_dept,name='destroy_dept'),
    path('students/', views.student_view, name='students'),
    path('edit-students/<int:id>', views.edit_student_view, name='edit_student_view'),
    path('edit-teachers/<int:id>', views.edit_teacher_view, name='edit_teacher_view'),
    path('updateteacherspage/<int:id>', views.updateteacherspage,name='updateteacherspage'),

    
    path('teachers/', views.teacher_view, name='teachers'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)