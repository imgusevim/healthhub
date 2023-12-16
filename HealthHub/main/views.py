from django.shortcuts import render

def index(request):
    return render(request,'main/index.html')


def eating(request):
    return render(request,'main/eating.html')


def training(request):
    return render(request,'main/training.html')


def profile(request):
    return render(request,'main/profile.html')

