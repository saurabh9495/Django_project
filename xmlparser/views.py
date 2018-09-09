from django.shortcuts import render

def index(request):
    return render(request, 'xmlparser/home.html')

def record(request):
    return render(request, 'xmlparser/recorded.html')

def output(request):
    return render(request, 'xmlparser/record.html')