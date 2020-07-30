from django import forms

from .models import Personal,Education,Employment,Project,Skill,Certificate


class PersonalForm(forms.ModelForm):
    class Meta:
        model=Personal
        fields=('name','phone','email','address','intro',)

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields= ('institution_name','city','state','degree','stream','percentage_or_cg','graduation_year',)

class EmploymentForm(forms.ModelForm):
    class Meta:
        model=Employment
        fields= ('employer','job_title','description','city','state','start_month','start_year','presently_working',
                 'end_month','end_year',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields= ('project_title','project_link','project_code_link','description',)

class SkillForm(forms.ModelForm):
    class Meta:
        model=Skill
        fields= ('skill_name','skill_rating',)

class CertificateForm(forms.ModelForm):
    class Meta:
        model=Certificate
        fields= ('certificate_title','organization','month','year','description',)
