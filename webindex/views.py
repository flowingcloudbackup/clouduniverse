from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    return render(request, 'MyFlatUI/MyIndex.html')

def redirect(request):
    return HttpResponseRedirect('/index')
