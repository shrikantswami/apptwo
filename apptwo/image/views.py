from django.shortcuts import render
from image.models import Topic,data
from image.forms import user_sign
#from django.http import HttpResponse
def pics(request):
    wb_name = data.objects.order_by('date')
    my_dict= {'name_list': wb_name}
    return  render(request,'apptwo/index.html',context=my_dict)

def formPage(request):
    page = user_sign()
    if request.method == 'POST':
        page_post = user_sign(request.POST)
        if page_post.is_valid():
            page_post.save(commit=True)
            return render(request,'apptwo/user_form.html',{'form':page})
        else :
            return render(request,'apptwo/user_form.html',{'form':"Enter Valid Deails"})
    return render(request,'apptwo/user_form.html',{'form':page})


# Create your views here.
