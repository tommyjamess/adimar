from django.shortcuts import render, redirect
from products.models import Product, Category, Mcategory, Customimg, Loveit
from home.models import Setting
from order.models import Cart

# Create your views here.
def content(request):

    return render(request, 'product/prod.html' )

def detail(request, id):
    setting = Setting.objects.get(pk=1)
    detail = Product.objects.get(id=id)
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    colors = Product.objects.get(pk=id)
    loves = Loveit.objects.filter(product_id=id).count()
    related = Product.objects.filter(category__id=id)
    

    context = {
        'setting': setting,
        'detail': detail,
        'mcat': mcat,
        'colors':colors,
        'cart': shopcart,
        'loves': loves,
        'related': related,
    }

    return render(request, 'product/detail.html', context)

def bulk(request, id):
    setting = Setting.objects.get(pk=1)
    detail = Product.objects.get(id=id)
    mcat = Mcategory.objects.all()
    

    context = {
        'setting': setting,
        'detail': detail,
        'mcat': mcat,
    }

    return render(request, 'product/bulk.html', context)


def products(request):
    setting = Setting.objects.get(pk=1)
    prod = Product.objects.filter(order="main").order_by('?')[:50]
    cat = Category.objects.all()
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    


    context = {
        'setting': setting,
        'products': prod,
        'cat': cat,
        'mcat': mcat,
        'cart': shopcart,
    }
    return render(request, 'product/products.html', context)

def filt(request, id):
    setting = Setting.objects.get(pk=1)
    filt = Product.objects.filter(category__id=id)
    mcat = Mcategory.objects.all()
    cat = Category.objects.all()
    title = Category.objects.get(pk=id)
    
    context = {
        'setting': setting,
        'filt': filt,
        'mcat': mcat,
        'cat': cat,
        'title':title,
    }

    return render(request, 'product/filter.html', context)

def mcat(request, slug, id):
    setting = Setting.objects.get(pk=1)
    products = Product.objects.filter(mcat__id=id).order_by('?')[:50]
    gallery = Product.objects.filter(mcat__id=id)
    mcat = Mcategory.objects.all()
    cat = Category.objects.filter(clist=True)
    shopcart = Cart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    
    
    context = {
        'setting': setting,
        'products': products,
        'mcat': mcat,
        'title': slug,
        'cat': cat,
        'gallery': gallery,
        'cart': shopcart,
    }

    return render(request, 'product/mcat.html', context)


def gallery(request):
    products = Product.objects.filter(order='custom').order_by('?')[:10]
    setting = Setting.objects.get(pk=1)
    cat = Category.objects.filter(clist=True)
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(user__username=request.user.username)
    


    context = {
        'setting': setting,
        'gallery': products,
        'cat': cat,
        'mcat': mcat,
        'cart': shopcart,
    }

    return render(request, 'product/gallery.html', context)

def gallerydet(request, id):

    gdetail = Product.objects.get(id=id)
    setting = Setting.objects.get(pk=1)
    mcat = Mcategory.objects.all()
    shopcart = Cart.objects.filter(order_placed=False).filter(user__username=request.user.username)

    context = {
        'gdetail': gdetail,
        'mcat': mcat,
        'cart': shopcart,
        'setting': setting,
    }

    return render(request, 'product/gdetail.html', context)

def customized(request):
    setting = Setting.objects.get(pk=1)
    mcat = Mcategory.objects.all()
    image = Customimg.objects.order_by('?')[:1]

    context = {
        'setting':setting,
        'mcat': mcat,
        'image': image,
    }

    return render(request, 'product/custom.html', context)


def loveit(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        savelove = Loveit()
        savelove.value = 'love'
        savelove.product_id = request.POST.get('prod')
        
        savelove.save()
        
        return redirect(url)

