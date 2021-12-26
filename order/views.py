from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from home.models import Setting
from products.models import *
from order.models import *
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views import View
from user.forms import BillingForm
from user.models import BillingInfo
from django.conf import settings
from payments.models import DelFee, ShippingFee
from django.contrib.auth.decorators import login_required


import uuid
import random
import requests
import json
import string

# Create your views here.

@login_required(login_url='user:user-login')
@require_POST
def addtocart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    thesize = request.POST.get('size')
    theprodid = request.POST['prodid']
    thecolor = request.POST['color']
    aprod = Product.objects.get(pk=theprodid)

    cart = Cart.objects.filter(order_placed=True).filter(
        user__username=request.user.username)

    if cart:
        prodchecker = Cart.objects.filter(product__id=aprod.id, size=thesize, quantity=thequantity,
                                          color=thecolor, user__username=request.user.usernme).first()

        if prodchecker:
            prodchecker.quantity += thequantity
            prodchecker.size = thesize
            prodchecker.color = thecolor
            prodchecker.save()
        else:
            anitem = Cart()
            anitem.product = aprod
            anitem.user = request.user
            anitem.order_code = cart[0].order_code
            anitem.quantity = thequantity
            anitem.size = thesize
            anitem.color = thecolor
            anitem.order_palced = False
            anitem.save()

    else:
        ordercode = str(uuid.uuid4())
        newcart = Cart()
        newcart.product = aprod
        newcart.user = request.user
        newcart.size = thesize
        newcart.quantity = thequantity
        newcart.color = thecolor
        newcart.order_code = ordercode
        newcart.order_placed = False
        newcart.save()

    messages.info(request, 'The product has been added to your shopcart')
    return redirect(url)


@login_required(login_url='user:user-login')
def cart(request):
    setting = Setting.objects.get(pk=1)
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(
        user__username=request.user.username)
    delfee = DelFee.objects.get(pk=1)

    if ShippingFee.objects.filter(user=request.user).exists():
        shipfee = ShippingFee.objects.get(user=request.user)
        shippingfee = shipfee.price
    else:
        shippingfee = 0
    subtotal = 0
    vat = 0
    total = 0

    for item in shopcart:
        if item.product.dis_price:
            subtotal += item.product.dis_price * item.quantity
        else:
            subtotal += item.product.price * item.quantity


    total = subtotal + shippingfee

    context = {
        'setting': setting,
        'mcat': mcat,
        'cart': shopcart,
        'shippingfee': shippingfee,
        'vat': vat,
        'total': total,
        'subtotal': subtotal,
        'shipping': shippingfee,
        'delfee': delfee,
    }

    return render(request, 'order/cart.html', context)


@login_required(login_url='user:user-login')
@require_POST
def updatequantity(request):
    url = request.META.get('HTTP_REFERER')
    newquantity = request.POST['itemquantity']
    theitem = Cart.objects.get(id=request.POST['itemid'])
    theitem.quantity = newquantity
    theitem.save()

    return redirect(url)

@login_required(login_url='user:user-login')
def delete(request, id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    return redirect(url)


@login_required(login_url='user:user-login')
def checkout(request):
    url = request.META.get('HTTP_REFERER')
    if BillingInfo.objects.filter(user=request.user).exists():
        form = BillingForm( instance=request.user.billinginfo)
        if request.method == 'POST':
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            street = request.POST['street']
            neareststop = request.POST['nearest_stop']
            state = request.POST['state']
            city = request.POST['city']
            phoneone = request.POST['phone_one']
            phonetwo = request.POST['phone_two']

            if BillingInfo.objects.filter(user=request.user).exists():
                info = request.user.billinginfo
                info.first_name = firstname
                info.last_name = lastname
                info.street = street
                info.nearest_stop = neareststop
                info.state = state
                info.city = city
                info.phone_one = phoneone
                info.phone_two = phonetwo
                info.save()
                messages.info(request, 'Billing information has been updated')
                return redirect(url)

    else:
        form = BillingForm()
        if request.method == 'POST':
            firstname = request.POST['first_name']
            lastname = request.POST['last_name']
            street = request.POST['street']
            neareststop = request.POST['nearest_stop']
            state = request.POST['state']
            city = request.POST['city']
            phoneone = request.POST['phone_one']
            phonetwo = request.POST['phone_two']

            
            info = BillingInfo()
            info.first_name = firstname
            info.last_name = lastname
            info.street = street
            info.nearest_stop = neareststop
            info.state = state
            info.city = city
            info.phone_one = phoneone
            info.phone_two = phonetwo
            info.user = request.user
            info.save()
            messages.info(request, 'Billing information has added')
            return redirect(url)
    

    check = Cart.objects.filter(order_placed=False).filter(
        user__username=request.user.username)
    shopcart = Cart.objects.filter(order_placed=False).filter(
        user__username=request.user.username)
    mcat = Mcategory.objects.all()
    setting = Setting.objects.get(pk=1)
    delfee = DelFee.objects.get(pk=1)

    for item in shopcart:
        order_code = item.order_code

    if ShippingFee.objects.filter(user=request.user).exists():
        shipfee = ShippingFee.objects.get(user=request.user)
        shippingfee = shipfee.price
    else:
        shippingfee = 4000
    subtotal = 0
    vat = 0
    total = 0

    for item in shopcart:
        if item.product.dis_price:
            subtotal += item.product.dis_price * item.quantity
        else:
            subtotal += item.product.price * item.quantity


    total = subtotal + shippingfee



    context = {
        'check': check,
        'vat': vat,
        'subtotal': subtotal,
        'shippingfee': shippingfee,
        'total': total,
        'form': form,
        'cart': shopcart,
        'mcat': mcat,
        'setting': setting,
        'delfee': delfee,
        'order_code': order_code,
    }

    return render(request, 'order/checkout.html', context)


@login_required(login_url='user:user-login')
def deliverydata(request):
    if request.method == 'POST':
        locform = request.POST['delfee']
        checkcity = request.POST['checkcity']
        if ShippingFee.objects.filter(user=request.user).exists():
            locdata = request.user.shippingfee
            locdata.price = locform
            locdata.city = checkcity
            locdata.save()
            return redirect('order:order-checkout')
        else:
            locdata = ShippingFee()
            locdata.user = request.user
            locdata.price = locform
            locdata.save()
            return redirect('order:order-checkout')



@login_required(login_url='user:user-login')
@require_POST
def placeorder(request):
    if ShippingFee.objects.filter(user=request.user).exists():
        api_key = settings.SECRET_KEY
        url = 'https://api.paystack.co/transaction/initialize'
        callback_url = 'http://127.0.0.1:8000/payments/verify_payment/'
        ordernumber = request.POST['ordernumber']
        total = float(request.POST['amount']) * 100
        email = request.POST['email']
        autogen_ref = ''.join(random.choices(
            string.digits + string.ascii_letters, k=8))
        while Order.objects.filter(order_code=autogen_ref) is None:
            autogen_ref = ''.join(random.choices(
            string.digits + string.ascii_letters, k=8))

        current_user = User.objects.get(username=request.user.username)
        user = BillingInfo.objects.get(user__id=current_user.id)

        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': autogen_ref, 'amount': int(
            total), 'currency': 'NGN', 'order_number': ordernumber, 'email': email, 'callback_url': callback_url}

        try:
            r = requests.post(url, headers=headers, json=data)
        except Exception:
            messages.error(request, 'Make sure you have an internet connection and please try again')
        else:
            transback = json.loads(r.text)
            rd_url = transback['data']['authorization_url']
            order = Order()
            cart = Cart()
            
            theuser = BillingInfo.objects.filter(user=request.user).last()
            shopcart = Cart.objects.filter(user=request.user)
            for item in shopcart:
                Order.objects.create(
                    user=request.user, 
                    product=item.product,
                    quantity=item.quantity,
                    color=item.color,
                    size=item.size,
                    order_code=item.order_code, 
                    order_placed=True, 
                    payment_code=autogen_ref,
                    price=item.product.price
                ) 

            return redirect(rd_url)
        
        return redirect('order:order-checkout')
    
    else:

        return redirect('order:order-checkout')
        messages.error(request, "Please pick a delivery location")
    
        context = {
            'messages': messages,
        }
    
    return render(request, 'order/checkout.html', context)



    



