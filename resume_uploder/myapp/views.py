from django.shortcuts import render,HttpResponse
from .forms import ResumeForm
from .models import Resume

def index(request):
    if request.method=="POST":
        fm=ResumeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return HttpResponse('data save')
        else:
            return HttpResponse('error')
    fm=ResumeForm()
    candidate=Resume.objects.all()
    return render (request,'index.html',{'candidate':candidate,'form':fm})
def Candidate(request,pk):
    if request.method=='GET':
        candidate=Resume.objects.get(pk=pk)
    return render(request,'candidate.html',{'candidate':candidate})