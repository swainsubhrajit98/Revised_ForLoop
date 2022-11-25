from django.shortcuts import render

# Create your views here.
def A1_First(request):
    d={'a':10,'b':15,}
    return render(request,'A1_First.html',d)

def A1_Second(request):
    d={'a':10,'b':10}
    return render(request,'A1_Second.html',d)