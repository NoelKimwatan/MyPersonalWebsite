from django.shortcuts import render
from .models import About
from project.models import Project
from resume.models import Experience,Education,Certification,Resume


def index(request):
    abouts = About.objects.all()
    projects = Project.objects.all().order_by("id")
    resumes = Resume.objects.all()

    experiences = Experience.objects.all().order_by("-start_date")
    educations = Education.objects.all().order_by("-start_date")
    certifications = Certification.objects.all().order_by("-date_earned")


    
    return render(request,"index.html",{"projects":projects,"experiences":experiences,"educations":educations,"certifications":certifications,"abouts":abouts,"resumes":resumes})
    

def blog(request):
    return render(request,"blog.html")


def view_404(request,exception):
    return render(request,"error.html")