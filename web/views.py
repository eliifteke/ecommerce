from django.shortcuts import render

# Create your views here.
from service.models import KategoriModel, AltKategoriModel


def index(request):
    kategoriler = KategoriModel.objects.all()
    return render(request,'pages/index.html' , {'kategoriler': kategoriler})


def kategoriler(request , slug = None):
    kats = KategoriModel.objects.all()
    if  slug is None:
        return render(request , 'pages/kategoriler.html' , {'kategoriler':kats})
    else :
        kategori = KategoriModel.objects.get(slug=slug)
        return render(request , 'pages/kategoriler.html' ,  {'kategoriler':kats , 'kategori':kategori})