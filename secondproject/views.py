from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello World!")

# def test(request):
#     return HttpResponse("Test Page")


def index(request):
    mycontext={"name": "Ramos", "Age": 25}
    return render(request, 'secondpage/index.html', mycontext)
