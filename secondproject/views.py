from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

# def test(request):
#     return HttpResponse("Test Page")


def index(request):
    mycontext={"name": "Ramos", "Age": 25, "size":5232132135746755}
    return render(request, 'secondpage/index.html', mycontext)

def about(request):
    return render(request, 'secondpage/about.html')