from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome!')

def cordinate(request):
    return HttpResponse('Cordinate')