from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'index.html')