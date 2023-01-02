from http.client import HTTPResponse
from django.shortcuts import render
from .models import About_detail, Category, Project, ProjectImages, UploadDocument
from django.core.mail import BadHeaderError, send_mail
from django.http.response import JsonResponse

def index(request):
    cat = Category.objects.all()
    for_frontend = {
        'category': cat,
    }
    return render(request,'polls/index.html', for_frontend)

def about(request):
    try:
        ad = About_detail.objects.first()
        cat = Category.objects.all()
        doc = UploadDocument.objects.get(name="CV").file
        for_frontend = {
            'ad': ad,
            'category': cat,
            'doc_cv': doc,
        }
        return render(request,'polls/about.html', for_frontend)
    except FileNotFoundError as e:
        return error_page(request)
    except FileExistsError as e:
        return error_page(request)
    except Exception as e:
         return error_page(request)

def my_stack(request):
    cat = Category.objects.all()
    for_frontend = {
        'category': cat,
    }
    return render(request,'polls/mywork.html', for_frontend)

def my_project(request, category_slug):
    cat = Category.objects.all()
    unique_slug = Category.objects.get(slug = category_slug)
    project = Project.objects.all()
    
    def get_project(a, b):
     for item in a:
        if(b == item.category):
            return item
   
    check_cat = get_project(project, unique_slug)

    for_frontend = {
        'post': unique_slug,
        'category': cat,
        'project': project,
        'check': check_cat,
    }
    
    return render(request, 'polls/project.html', for_frontend)

def project_detail(request, category_slug, project_slug):
    project = Project.objects.get(slug=project_slug)
    cat = Category.objects.all()
    project_images = ProjectImages.objects.filter(project=project)

    for_frontend = {
        'project': project,
        'category': cat,
        'project_images': project_images
    }
    return render(request, 'polls/project_detail.html', for_frontend)


def contact(request):
    cat = Category.objects.all()
    for_frontend = {
        'category': cat,
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
            return HTTPResponse('Invalid header found.')
        
    return render(request,'polls/contact.html', for_frontend)

def post_json(request):
    #  data = list(AImages.objects.values()) + list(Category.objects.values())
    return render(request,'polls/about.html')
    #  return JsonResponse(data, safe=False)

def error_page(request):
    return render(request, 'polls/error.html')