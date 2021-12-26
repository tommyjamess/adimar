from django.shortcuts import render, redirect
from user.forms import CreateUserForm, AuthForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from home.models import Setting
from products.models import Mcategory
from django.contrib.auth.views import LoginView
from order.models import OrderPlaced, Order
from django.contrib.auth.decorators import login_required
from home.decorators import allowed_users
from django.contrib.auth import update_session_auth_hash 

# Create your views here.
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:user-login')
        else:
            form = CreateUserForm()


    setting = Setting.objects.get(pk=1)
    mcat = Mcategory.objects.all()

    context = {
        'form': form,
        'setting':setting,
        'mcat': mcat,
    }
    return render(request, 'user/signup.html', context)


class Login(LoginView):
    template_name = 'user/login.html'
    form_class = AuthForm
    success_url = 'home-index'
       

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["setting"] = Setting.objects.get(pk=1)
        context["mcat"] = Mcategory.objects.all()
        return context



@login_required(login_url='user:user-login')
@allowed_users(allowed_roles=['admin'])
def staffside(request):
    neworder = OrderPlaced.objects.filter(status="New")
    deliveredorder = OrderPlaced.objects.filter(status="Delivered")
    onshipping = OrderPlaced.objects.filter(status="Onshipping")
    totalorders = OrderPlaced.objects.all()
    preparing = OrderPlaced.objects.filter(status="Preparing")


    context = {
        'neworder': neworder,
        'deliveredorder': deliveredorder,
        'onshipping': onshipping,
        'preparing': preparing,
        'totalorders': totalorders,
    }
    

    return render(request, 'user/staff.html', context)



@login_required(login_url='user:user-login')
@allowed_users(allowed_roles=['admin'])
def neworders(request):
    neworder = OrderPlaced.objects.filter(status="New")
    orderproduct = Order.objects.filter(status="New")
    context = {
        'neworder': neworder,
        'orderproduct': orderproduct,
    }

    return render(request, 'user/new_orders.html', context)



@login_required(login_url='user:user-login')
@allowed_users(allowed_roles=['admin'])
def deliveredorders(request):
    deliveredorder = OrderPlaced.objects.filter(status="Delivered")
    orderproduct = Order.objects.filter(status="Delivered")
    context = {
        'deliveredorder': deliveredorder,
        'orderproduct': orderproduct,
    }

    return render(request, 'user/delivered_orders.html', context)




@login_required(login_url='user:user-login')
@allowed_users(allowed_roles=['admin'])
def onshipping(request):
    onshipping = OrderPlaced.objects.filter(status="Onshipping")
    orderproduct = Order.objects.filter(status="Onshipping")
    context = {
        'onshipping': onshipping,
        'orderproduct': orderproduct,
    }

    return render(request, 'user/onshipping.html', context)



@login_required(login_url='user:user-login')
@allowed_users(allowed_roles=['admin'])
def preparing(request):
    preparing = OrderPlaced.objects.filter(status="Preparing")
    orderproduct = Order.objects.filter(status="Preparing")
    context = {
        'preparing': preparing,
        'orderproduct': orderproduct,
    }

    return render(request, 'user/preparing.html', context)


@login_required(login_url='user:user-login')
@allowed_users(allowed_roles=['admin'])
def totalorders(request):
    totalorders = OrderPlaced.objects.all()
    context = {
        'totalorders': totalorders,
    }

    return render(request, 'user/totalorders.html', context)




    
