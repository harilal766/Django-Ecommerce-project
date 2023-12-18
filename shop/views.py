from django.shortcuts import render
from shop.models import Product,Category
from django.contrib.auth.decorators import login_required
#from cart.models import Cart

from django.contrib.auth.models import User # reg
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

import requests

# Create your views here.

response = requests.get("https://dummyjson.com/products")
prod_data = response.json()
def home(request):
    category=Category.objects.all()
    avail_cat = set()
    for i in prod_data['products']:
        avail_cat.add(i['category'])
    return render(request,'category.html',{'category':category,"avail_cat":avail_cat})

def category(request):
    p=Category.objects.all()
    print(p)
    return render(request,'category.html',{'c':p})

def products(request,cslug):
    p=Product.objects.filter(category__slug=cslug)
    c=Category.objects.get(slug=cslug)
    return render(request,'product.html',{'p':p,'c':c})
def categoryAPI(request):
    category=prod_data['products']
    return render(request,'categoryAPI.html',{'c':category})
def productsAPI(request,cslug):
    c=Category.objects.get(slug=cslug)
    p=Product.objects.filter(category__slug=cslug)
    return render(request,'productAPI.html',{'p':p,'c':c})

def prodetail(request,pslug):
    p=Product.objects.get(slug=pslug)
    return render(request,'prodetail.html',{'p':p})


def register(request):
    if(request.method=='POST'): # condition
        f=request.POST['f']
        l=request.POST['l']
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        if p==cp: # confirm entered credentials
            user = User.objects.create_user(first_name=f,last_name=l,username=u,password=p,)# model creation
            user.save() # saving created model
            return home(request)
    return render(request,'signup.html',)

def usersignin(request):
    if(request.method=='POST'):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            return home(request)
        else:
            messages.error(request,'Invalid credentials')

    return render(request,'login.html')

def usersignout(request):
    logout(request)
    return home(request)



from rest_framework import viewsets
from shop.serializers import ShopSerializer,UserSerializer
from shop.models import Product
from rest_framework.permissions import AllowAny

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = Product.objects.all()
    serializer_class = ShopSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny,]
    queryset = User.objects.all()
    serializer_class = UserSerializer


















