from django.shortcuts import render

def progeat(request):
    return render(request,'mlprograms/progeat.html')

def progtrain(request):
    return render(request,'mlprograms/progtrain.html')