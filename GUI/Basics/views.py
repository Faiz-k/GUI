from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome")

def Aboutus(request):
    info = " My first django programming on 27/8/23"
    return render(request,'Aboutus.html',context={'info':info })

def Register(request):
    if(request.method=="POST"):
        data=request.POST
        firstname=data.get('txtfirstname')
        lastname=data.get('txtlastname')
        if('submit'in request.POST):
            result=firstname+" "+lastname
            return render(request,"Register.html",context={'result':result})
    return render(request,'Register.html')
def Calculator(request):
    if(request.method=="POST"):
        data=request.POST
        fnum=data.get('txtfirstname')
        lnum=data.get('txtlastname')
        if(len(fnum)<1):
            result="Enter the first number "
            return render(request,"Calculator.html",context={'result':result})
        if(len(lnum)<1):
            result="Enter the second number "
            return render(request,"Calculator.html",context={'result':result})
        fnum=int(fnum)
        lnum=int(lnum)
        if('ADD'in request.POST):
            result=fnum+lnum
            return render(request,"Calculator.html",context={'result':result})
        if('SUB'in request.POST):
            result=fnum-lnum
            return render(request,"Calculator.html",context={'result':result})
        if('MUL'in request.POST):
            result=fnum*lnum
            return render(request,"Calculator.html",context={'result':result})
        if('DIV'in request.POST):
            result=fnum/lnum
            return render(request,"Calculator.html",context={'result':result})
    

    return render(request,'Calculator.html')