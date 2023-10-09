from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_task

# Create your views here.

def index(request, *args, **kwargs):
    test_task.delay()
    return HttpResponse("Done")
