from django.shortcuts import render

# Create your views here.


#view ki jere pay akey la
def byenvini (request) :
 return render(request,'welcome.html')