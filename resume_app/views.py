from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Personal,Education,Employment,Project,Skill,Certificate
from .forms import PersonalForm,EducationForm,EmploymentForm,ProjectForm,SkillForm,CertificateForm

def index(requests):
    return render(requests,'resume_app/index.html')

def new_personal_info(request):
    flag=0
    a=Personal.objects.all()
    for i in a:
        if i.user == request.user:
            flag=1
            break
    if flag == 1:
        pk = request.user.personals.pk
        personal = get_object_or_404(Personal, pk=pk)
        if request.method == 'POST':
            form = PersonalForm(request.POST, instance=personal)
            if form.is_valid:
                student = form.save(commit=False)
                student.user = request.user
                student.save()
                return redirect('educational_list')
        else:
            form = PersonalForm(instance=personal)
        return render(request, 'resume_app/personal_edit.html', {'form': form})

    else:
        if request.method == 'POST':
            form = PersonalForm(request.POST)
            if form.is_valid:
                student = form.save(commit=False)
                student.user = request.user
                student.save()
                return redirect('educational_list')
        else:
            form = PersonalForm()
        return render(request, 'resume_app/personal_edit.html', {'form': form})


def educational_list(request):
    lists = Education.objects.filter(user=request.user)
    return render(request,'resume_app/educational_list.html',{'lists':lists})

def new_educational_info(request):
    if request.method=='POST':
        form=EducationForm(request.POST)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('educational_list')
    else:
        form=EducationForm()
    return render(request,'resume_app/educational.html',{'form':form})

def update_educational_info(request,pk):
    institution = Education.objects.get(pk=pk)
    if request.method=='POST':
        form=EducationForm(request.POST,instance=institution)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('educational_list')
    else:
        form=EducationForm(instance=institution)
    return render(request,'resume_app/educational.html',{'form':form})

def delete_educational_info(request,pk):
    institution=get_object_or_404(Education,pk=pk)
    institution.delete()
    return redirect('educational_list')

def employment_list(request):
    lists = Employment.objects.filter(user=request.user)
    return render(request,'resume_app/employment_list.html',{'lists':lists})

def new_employment_info(request):
    if request.method=='POST':
        form=EmploymentForm(request.POST)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('employment_list')
    else:
        form=EmploymentForm()
    return render(request,'resume_app/employment.html',{'form':form})

def update_employment_info(request,pk):
    institution = Employment.objects.get(pk=pk)
    if request.method=='POST':
        form=EmploymentForm(request.POST,instance=institution)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('employment_list')
    else:
        form=EmploymentForm(instance=institution)
    return render(request,'resume_app/employment.html',{'form':form})

def delete_employment_info(request,pk):
    institution=get_object_or_404(Employment,pk=pk)
    institution.delete()
    return redirect('employment_list')

def project_list(request):
    lists = Project.objects.filter(user=request.user)
    return render(request,'resume_app/project_list.html',{'lists':lists})

def new_project_info(request):
    if request.method=='POST':
        form=ProjectForm(request.POST)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('project_list')
    else:
        form=ProjectForm()
    return render(request,'resume_app/project.html',{'form':form})

def update_project_info(request,pk):
    institution = Project.objects.get(pk=pk)
    if request.method=='POST':
        form=ProjectForm(request.POST,instance=institution)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('project_list')
    else:
        form=ProjectForm(instance=institution)
    return render(request,'resume_app/project.html',{'form':form})


def delete_project_info(request,pk):
    institution=get_object_or_404(Project,pk=pk)
    institution.delete()
    return redirect('project_list')

def skill_list(request):
    lists = Skill.objects.filter(user=request.user)
    return render(request,'resume_app/skill_list.html',{'lists':lists})

def new_skill_info(request):
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('skill_list')
    else:
        form=SkillForm()
    return render(request,'resume_app/skill.html',{'form':form})

def update_skill_info(request,pk):
    institution = Skill.objects.get(pk=pk)
    if request.method=='POST':
        form=SkillForm(request.POST,instance=institution)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('skill_list')
    else:
        form=SkillForm(instance=institution)
    return render(request,'resume_app/skill.html',{'form':form})

def delete_skill_info(request,pk):
    institution=get_object_or_404(Skill,pk=pk)
    institution.delete()
    return redirect('skill_list')

def certificate_list(request):
    lists = Certificate.objects.filter(user=request.user)
    return render(request,'resume_app/certificate_list.html',{'lists':lists})

def new_certificate_info(request):
    if request.method=='POST':
        form=CertificateForm(request.POST)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('certificate_list')
    else:
        form=CertificateForm()
    return render(request,'resume_app/certificate.html',{'form':form})

def update_certificate_info(request,pk):
    institution = Certificate.objects.get(pk=pk)
    if request.method=='POST':
        form=CertificateForm(request.POST,instance=institution)
        if form.is_valid:
            student=form.save(commit=False)
            student.user=request.user
            student.save()
            return redirect('certificate_list')
    else:
        form=CertificateForm(instance=institution)
    return render(request,'resume_app/certificate.html',{'form':form})

def delete_certificate_info(request,pk):
    institution=get_object_or_404(Certificate,pk=pk)
    institution.delete()
    return redirect('certificate_list')

