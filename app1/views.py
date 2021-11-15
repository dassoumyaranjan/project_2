from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
def love(request):
    return HttpResponse('<h1><marquee>Dhoni is Best Finisher</marquee></h1>')
    