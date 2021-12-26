from django.shortcuts import render
from home.models import Setting
from products.models import Product, Mcategory
from order.models import Cart

# Create your views here.
def index(request):
    setting = Setting.objects.get(pk=1)
    product = Product.objects.filter(banner=True)
    adire = Product.objects.filter(adire=True).order_by('?')[:15]
    bag = Product.objects.filter(bags=True).order_by('?')[:15]
    urban = Product.objects.filter(urban_wear=True).order_by('?')[:15]
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    banner = Product.objects.filter(banner=True)
    

    context = {
        'setting': setting,
        'products': product,
        'adire': adire,
        'bags': bag,
        'urban': urban,
        'mcat': mcat,
        'cart':shopcart,
        'banner':banner,
    }

    return render(request, 'home/index.html', context)


