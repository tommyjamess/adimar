from django.shortcuts import render
from user.models import BillingInfo
from order.models import OrderPlaced, Cart, Order
from order.forms import OrderForm
from pypaystack import Transaction, Customer, Plan
from django.conf import settings
from home.models import Setting
from django.contrib import messages
from payments.models import DelFee, ShippingFee
from products.models import Mcategory
from django.contrib.auth.decorators import login_required


@login_required(login_url='user:user-login')
def verify(request):
    setting = Setting.objects.get(pk=1)
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(
        user__username=request.user.username)

    
    code = Order.objects.filter(user=request.user).last()
    
    reference = request.GET.get('reference')
    # ordernumber = request.GET.get('ordernumber')
    transaction = Transaction(authorization_key=settings.SECRET_KEY)
    response = transaction.verify(reference)
    confirm = response[3]["status"]


    setting = Setting.objects.get(pk=1)
    shopcart = Cart.objects.filter(
        order_placed=False).filter(user=request.user)
    delfee = DelFee.objects.get(pk=1)

    if ShippingFee.objects.filter(user=request.user).exists():
        shipperfee = ShippingFee.objects.get(user=request.user)
        shippingfee = shipperfee.price
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

    theuser = BillingInfo.objects.filter(user=request.user).last()

    if confirm == "success":
        OrderPlaced.objects.create(
            user=request.user,
            first_name = theuser.first_name,
            last_name = theuser.last_name,
            street = theuser.street,
            nearest_stop = theuser.nearest_stop,
            phone_one = theuser.phone_one,
            phone_two = theuser.phone_two,
            city = theuser.city,
            state = theuser.state,
            total = total,
            order_placed = True,
            order_code = code.order_code,
            payment_code = code.payment_code,
            payment_verified = True,
        )
        
        messages.success(request, 'Payment was successfull')
    else:
        messages.error(request, 'Payment was unsuccessfull, please try again!')
        return redirect('order:order-checkout')
        
    
    Cart.objects.filter(user=request.user).delete()


    context = {
        'setting': setting,
        'mcat': mcat,
        'cart': shopcart,
        
    }

    return render(request, 'payment/callback.html', context)



@login_required(login_url='user:user-login')
def callback(request):
    setting = Setting.objects.get(pk=1)
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(
        user__username=request.user.username)

    context = {
        'setting': setting,
        'mcat': mcat,
        'cart': shopcart,
        
    }

    return render(request, 'payment/callback.html', context)
