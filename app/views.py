from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request,'new.html')

def dashboard(request):
    return render(request,'dashboard.html')

def archives(request):
    return render(request,'archives.html')

