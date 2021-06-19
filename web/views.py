import resolved as resolved
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import resolve

from authentication.models import UserModel
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

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

"""
def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            print(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                print("if 'in içinde")
                login(request, user)
                return redirect("homepage_view")
            else:
                messages.error(request, 'username or password not correct')
                return redirect('error_message')
    context = {}
    return render(request, "index.html", context)  #html adı yazılır renderin içine
"""
def user_login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))

            return HttpResponse("Invalid login details given")
    else:
        return redirect("user_login")


def register(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        if password != password2:
            return HttpResponse("Password fields didn't match.")

        user = UserModel(username=username, first_name=first_name, last_name=last_name, email=email)  # create object
        user.set_password(password)
        user.save()
        return redirect('index')



