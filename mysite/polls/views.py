from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index1(request):
    return render(request,'index1.html')