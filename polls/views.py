from django.shortcuts import get_object_or_404, render
from .models import Category, Project, UploadDocument
from django.core.mail import BadHeaderError, send_mail
from django.http import JsonResponse
def index(request):
    for_frontend = {
        'category': Category.get_category_list(),
    }
    return render(request,'polls/index.html', for_frontend)

def about(request):
    for_frontend = {
        'category': Category.get_category_list(),
        'doc_cv': UploadDocument.get_cv(),
    }
    return render(request,'polls/about.html', for_frontend)

def my_stack(request):

    for_frontend = {
        'category': Category.get_category_list(),
    }
    return render(request,'polls/mywork.html', for_frontend)

def my_project(request, category_slug):
    unique_slug = get_object_or_404(Category, slug = category_slug)
    my_projects = Project.objects.all()   

    def get_project(a, b):
     for item in a:
        if(b == item.category):
            return item
            
    # Check that a category has projects in it
    check_cat = get_project(my_projects, unique_slug)

    for_frontend = {
        'post': unique_slug,
        'category': Category.get_category_list(),
        'project': my_projects,
        'check': check_cat,
    }
    
    return render(request, 'polls/project.html', for_frontend)

def project_detail(request, category_slug, project_slug):
    project = Project.objects.get(slug=project_slug)
    print(project)
    for_frontend = {
        'project': project,
        'category': Category.get_category_list(),
    }
    return render(request, 'polls/project_detail.html', for_frontend)


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

def post_json(request):
    data = list(Category.objects.values())
    return JsonResponse(data, safe=False)

