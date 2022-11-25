from django.shortcuts import render

# Create your views here.
def A2_First(request):
    d={'a':10,'b':30,'c':20}
    return render(request,'A2_First.html',d)

def A2_Second(request):
    d={'name':'SUBHRAJIT'}
    return render(request,'A2_Second.html',d)