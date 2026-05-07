from django.http import HttpResponse

def home(request):
    return HttpResponse("Team Task Manager By Pedagani Sai Teja")