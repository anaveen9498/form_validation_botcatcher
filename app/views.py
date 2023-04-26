from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.



def student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFOD=StudentForm(request.POST)
        if SFOD.is_valid():
            return HttpResponse(str(SFOD.cleaned_data))
        return HttpResponse('Not valid')

    return render(request,'student.html',d)
