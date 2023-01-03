from django.shortcuts import render

# Create your views here.
def conditions(request):
    #a=int(input('enter'))
    d={'a':66123,'b':220005,'c':2388}
    return render(request,'conditions.html',d)