from django.shortcuts import render
from image.models import Topic,data
#from django.http import HttpResponse
def pics(request):
    wb_name = data.objects.order_by('date')
    my_dict= {'name_list': wb_name}
    return  render(request,'apptwo/index.html',context=my_dict)


# Create your views here.
