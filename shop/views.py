from django.shortcuts import render
from shop.models import Product,Category
from django.contrib.auth.decorators import login_required
#from cart.models import Cart

from django.contrib.auth.models import User # reg
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,'index.html')

def category(request):
    p=Category.objects.all()
    print(p)
    return render(request,'index.html',{'c':p})

def products(request,cslug):
    p=Product.objects.filter(category__slug=cslug)
    c=Category.objects.get(slug=cslug)
    return render(request,'product.html',{'p':p,'c':c})

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


















