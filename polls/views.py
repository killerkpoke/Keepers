from django.shortcuts import render, redirect
from .models import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
def index(request):
    return render(request,'polls/index.html')

def about(request):
    return render(request,'polls/about.html')

def mywork(request):

    final_works = []

    #dbworks = Works.objects.all()
    
    #for x in dbworks:
    #    final_works.append((x.named, x.image))

    #for_frontend = {
    #    'final_works': final_works,
    #}
    return render(request,'polls/mywork.html')#,for_frontend)

def contact(request):
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
        
    return render(request,'polls/contact.html')
