from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict= {'insert_me':"it is from views.py"}
    return render(request,'music/index.html',context=my_dict)
# Create your views here.
