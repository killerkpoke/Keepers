from django.shortcuts import render, redirect
from .models import Category
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    for_frontend = {
        'category': Category.get_category_list(),
    }
    return render(request,'polls/index.html', for_frontend)

def about(request):
    for_frontend = {
        'category': Category.get_category_list(),
    }
    return render(request,'polls/about.html', for_frontend)

def mywork(request):

    for_frontend = {
        'category': Category.get_category_list(),
    }
        


    return render(request,'polls/mywork.html', for_frontend)

def contact(request):
    for_frontend = {
        'category': Category.get_category_list(),
    }
    if request.POST:
        contact_list = []
        request_data = request.POST
        for data in request_data.values():
            contact_list.append(data)
        Pname = contact_list[1]
        from_email = contact_list[2]
        subject = contact_list[3]
        message = contact_list[4] 
        try:
            send_mail(Pname+" - "+subject, message +"\nFrom : "+from_email, None, [' """your email address which receive others messages """ '], fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        
    return render(request,'polls/contact.html', for_frontend)
