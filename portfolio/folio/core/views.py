from django.shortcuts import render

# Create your views here.


#view ki jere pay akey la
def byenvini (request) :
 return render(request,'welcome.html')

def about (request) :
 return render(request,'about.html')

def projects (request) :
 return render(request,'project.html')

def skills (request) :
 return render(request,'skills.html')

