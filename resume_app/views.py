from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Personal,Education,Employment,Project,Skill,Certificate
from .forms import PersonalForm,EducationForm,EmploymentForm,ProjectForm,SkillForm,CertificateForm

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa


def index(requests):
    return render(requests,'resume_app/index.html')

@login_required
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

@login_required
def educational_list(request):
    lists = Education.objects.filter(user=request.user).order_by('-graduation_year')
    return render(request,'resume_app/educational_list.html',{'lists':lists})

@login_required
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

@login_required
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

@login_required
def delete_educational_info(request,pk):
    institution=get_object_or_404(Education,pk=pk)
    institution.delete()
    return redirect('educational_list')

@login_required
def employment_list(request):
    lists = Employment.objects.filter(user=request.user).order_by('-start_year').order_by('-start_month')
    return render(request,'resume_app/employment_list.html',{'lists':lists})

@login_required
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

@login_required
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

@login_required
def delete_employment_info(request,pk):
    institution=get_object_or_404(Employment,pk=pk)
    institution.delete()
    return redirect('employment_list')

@login_required
def project_list(request):
    lists = Project.objects.filter(user=request.user)
    return render(request,'resume_app/project_list.html',{'lists':lists})

@login_required
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

@login_required
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

@login_required
def delete_project_info(request,pk):
    institution=get_object_or_404(Project,pk=pk)
    institution.delete()
    return redirect('project_list')

@login_required
def skill_list(request):
    lists = Skill.objects.filter(user=request.user)
    return render(request,'resume_app/skill_list.html',{'lists':lists})

@login_required
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

@login_required
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

@login_required
def delete_skill_info(request,pk):
    institution=get_object_or_404(Skill,pk=pk)
    institution.delete()
    return redirect('skill_list')

@login_required
def certificate_list(request):
    lists = Certificate.objects.filter(user=request.user)
    return render(request,'resume_app/certificate_list.html',{'lists':lists})

@login_required
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

@login_required
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

@login_required
def delete_certificate_info(request,pk):
    institution=get_object_or_404(Certificate,pk=pk)
    institution.delete()
    return redirect('certificate_list')

def cv(request):
    user = request.user
    educations = Education.objects.filter(user=user).order_by('-graduation_year')
    employments = Employment.objects.filter(user=user).order_by('-start_year')
    certificates = Certificate.objects.filter(user=user).order_by('-year')
    return render(request,'resume_app/cv1.html',{'user':user,'educations':educations,'employments':employments,'certificates':certificates})


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
	    return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class ViewPDF(View):

    def get(self, request, *args, **kwargs):

        user = request.user
        educations = Education.objects.filter(user=user).order_by('-graduation_year')
        employments = Employment.objects.filter(user=user).order_by('-start_year')
        certificates = Certificate.objects.filter(user=user).order_by('-year')
        pdf = render_to_pdf('resume_app/cv1.html',
                    {'user': user, 'educations': educations, 'employments': employments, 'certificates': certificates})
        return HttpResponse(pdf, content_type='application/pdf')

