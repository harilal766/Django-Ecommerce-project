from django.shortcuts import render,redirect
from cart.models import Cart,Order,Account
from shop.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def cart_view(request):
    total=0
    try:
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity * i.products.price

    except Cart.DoesNotExist:
        pass
    return render(request,'cart.html',{'cart':cart,'total':total})

@login_required
def add_cart(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity<cart.products.stock:
            cart.quantity+=1
            cart.save()
    except:
        cart=Cart.objects.create(products=product,user=user,quantity=1) #main code
        cart.save()
    return redirect('cart:cart_view') #to go to verification

@login_required
def minus(request,p):
    product=Product.objects.get(id=p)
    user=request.user
    try:
        cart=Cart.objects.get(products=product,user=user)
        if cart.quantity>1:
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return redirect('cart:cart_view') #to go to verification

@login_required
def delete(request,p):
    u=request.user
    p=Product.objects.get(id=p)
    try:
        cart=Cart.objects.get(products=p,user=u)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')



@login_required
def order(request):
    total=0
    items=0
    if(request.method=='POST'):
        ad=request.POST['ad']
        ph=request.POST['ph']
        ac=request.POST['ac']
        user=request.user
        cart=Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity * i.products.price
            items+=i.quantity
        ##amount verification
        account=Account.objects.get(acc_number=ac)
        if float(account.amount) >= total:
            account.amount=account.amount-total
            account.save()
            ## deleting from cart after placing order
            for i in cart:
                order=Order.objects.create(user=user,products=i.products,address=ad,phone=ph,
                                           order_status='Paid',no_ofitems=i.quantity)
                order.save()
            cart.delete()
            msg='Order placed successfully'
            return render(request,'confirmation.html')
            # return render(request, 'orderdetail.html', {'address': ad, 'phone': ph, 'account': ac,'total':total,'items': items})
        else:
            msg="Insufficient Amount, you can't place order."
            return render(request,'orderdetail.html',{"msg":msg})
    return render(request,'order.html')

@login_required
def order_views(request):
    user=request.user
    o=Order.objects.filter(user=user,order_status='Paid')
    return render(request,'orderview.html',{"o":o})