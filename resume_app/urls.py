from django.urls import path
from . import views
from .views import ViewPDF


urlpatterns = [
    path('',views.index,name='index'),
    path('new_personal_info/',views.new_personal_info,name = 'new_personal_info'),
    path('educational_list/',views.educational_list,name = 'educational_list'),
    path('new_educational_info/',views.new_educational_info,name = 'new_educational_info'),
    path('update_educational_info/<int:pk>', views.update_educational_info, name='update_educational_info'),
    path('delete_educational_info/<int:pk>', views.delete_educational_info, name='delete_educational_info'),
    path('employment_list/',views.employment_list,name = 'employment_list'),
    path('new_employment_info/',views.new_employment_info,name = 'new_employment_info'),
    path('update_employment_info/<int:pk>', views.update_employment_info, name='update_employment_info'),
    path('delete_employment_info/<int:pk>', views.delete_employment_info, name='delete_employment_info'),
    path('project_list/',views.project_list,name = 'project_list'),
    path('new_project_info/',views.new_project_info,name = 'new_project_info'),
    path('update_project_info/<int:pk>', views.update_project_info, name='update_project_info'),
    path('delete_project_info/<int:pk>', views.delete_project_info, name='delete_project_info'),
    path('skill_list/',views.skill_list,name = 'skill_list'),
    path('new_skill_info/',views.new_skill_info,name = 'new_skill_info'),
    path('update_skill_info/<int:pk>', views.update_skill_info, name='update_skill_info'),
    path('delete_skill_info/<int:pk>', views.delete_skill_info, name='delete_skill_info'),
    path('certificate_list/',views.certificate_list,name = 'certificate_list'),
    path('new_certificate_info/',views.new_certificate_info,name = 'new_certificate_info'),
    path('update_certificate_info/<int:pk>', views.update_certificate_info, name='update_certificate_info'),
    path('delete_certificate_info/<int:pk>', views.delete_certificate_info, name='delete_certificate_info'),

    path('cv/',views.cv,name='cv'),
    path('viewpdf/',ViewPDF.as_view(),name='viewpdf'),


]
