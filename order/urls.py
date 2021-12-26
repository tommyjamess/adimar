from django.urls import path

from . import views 

app_name = 'order'


urlpatterns = [
    path('addtocart/', views.addtocart, name='order-addtocart'),
    path('updatequnatity/', views.updatequantity, name='order-updatequantity'),
    path('deletefromcart/<str:id>', views.delete, name= 'order-delete-item'),
    path('shopcart', views.cart, name='order-cart'),
    path('checkout/', views.checkout, name='order-checkout'),
    path('place-order/', views.placeorder, name='order-placeorder'),
    path('deliverydata', views.deliverydata, name='deliverydata'),
]
