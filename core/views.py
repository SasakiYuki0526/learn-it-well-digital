from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def project(request):
    return render(request, 'project.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def login(request):
    return render(request, 'login.html')


def forgetPwd(request):
    return render(request, 'ForgetPwd.html')


def register(request):
    return render(request, 'register.html')


def Udetail(request):
    return render(request, 'UserDetail.html')


def sroom(request):
    return render(request, 'StudyRoom.html')


def droom(request):
    return render(request, 'DiscusRoom.html')


def achievement(request):
    return render(request, 'achievement.html') #完成


def report(request):
    return render(request, 'report.html') #完成


def Splan(request):
    return render(request, 'StudyPlan.html')