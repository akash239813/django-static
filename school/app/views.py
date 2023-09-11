from django.shortcuts import render,redirect

# Create your views here.


def home(req):
     return render(req,'app/home.html')

def about(req):
    return render(req,'app/about.html')

def admission(req):
    return render(req,'app/admission.html')

def learning(req):
    data=[
        {
            'class':'9th',
            'fees':12000
        },
        {
            'class':'10th',
            'fees':15000
        },
        {
            'class':'11th',
            'fees':17000
        },
        {
            'class':'12th',
            'fees':20000
        }
       
    ]
    return render(req,'app/learning.html',{'data':data})

def newsevents(req):
    return render(req,'app/newsevents.html')

def parents(req):
    return render(req,'app/parents.html')