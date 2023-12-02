from django.shortcuts import render
from . models import Update,Award,Bussiness_Sector,Gallery
from .forms import ContactForm,IndexForm
from django.http import JsonResponse


  
# Create your views here.



def about(request):
    context = {"is_about": True}
    return render(request, "web/about.html", context)



def blogdetails(request):
    context = {
        "is_blog": True
    }
    return render(request , "web/blog-details.html",context)



def blog(request):
    one=Update.objects.all()
    context = {
        'is_blog': True,
        'update': one, 
    }
    return render(request , "web/blog.html",context)



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})
    else:
        form = ContactForm()
    
    context = {"is_contact": True, "form": form}
    return render(request, "web/contact.html", context)



def gallery(request):
    image = Gallery.objects.all()
    context = {
        'is_gallery': True,
        'images' : image,
    } 
    return render(request, 'web/gallery.html', context)



def index(request):
    one=Award.objects.all()
    two=Update.objects.all()
    if request.method == "POST":
        form = IndexForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False})
    else:
        form = IndexForm()
    
    context = {
        "is_index": True, 
        "form": form,
        'award': one,
        'update': two, 
        }
    return render(request, "web/index.html", context)



def servicesdetails(request):
    one=Bussiness_Sector.objects.all()
    context = {
        "is_servicesdetails": True,
        'Bussiness_Sector': one,
    }
    return render(request , "web/services-details.html",context)



def services(request):
    one=Award.objects.all()
    context = {
        'is_services': True,
        'award': one, 
    }
    return render(request , "web/services.html",context)



def singleservice(request):
    context = {"is_single-service": True}
    return render(request , "web/single-service.html",context)


def index2(request):
    return render(request , "web/index-2.html")





