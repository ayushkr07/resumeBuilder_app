from django.shortcuts import render

def index(requests):
    return render(requests,'resume_app/index.html')