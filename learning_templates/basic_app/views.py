from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {"text": "Hello Univers", "number": 240}
    return render(request, 'basic_app/index.html', context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def medative(request):
    return render(request, 'basic_app/medative.html')
