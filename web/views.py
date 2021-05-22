import resolved as resolved
from django.shortcuts import render

# Create your views here.
from django.urls import resolve

from service.models import KategoriModel, AltKategoriModel


def index(request):
    kategoriler = KategoriModel.objects.all()
    return render(request,'pages/index.html',{'kategoriler': kategoriler})


def kategoriler(request , slug = None):
    kats = KategoriModel.objects.all()
    # if request.method == "POST":

    # if resolve(request.path_info).url_name == "kategorislug":
    if  slug is None:
        return render(request , 'pages/kategoriler.html' , {'kategoriler':kats})
    else :
        kategori = KategoriModel.objects.get(slug=slug)
        return render(request , 'pages/kategoriler.html' ,  {'kategoriler':kats , 'kategori':kategori})

def elisi (request, slug = None):
    if slug is None:
     return render(request, "pages/elisi.html")