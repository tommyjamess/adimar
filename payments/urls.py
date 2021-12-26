from django.urls import path

from . import views 

app_name = 'payments'

urlpatterns = [
    path('verify_payment/', views.verify, name='payment-verify'),
    path('callback/', views.callback, name='payments-callback'),
]
