from django.urls import path

from . import views
from user.views import Login

app_name = 'user'

urlpatterns =[
    path('login/', Login.as_view(), name='user-login'),
    path('staff_side/', views.staffside, name='staffside'),
    path('new_orders/', views.neworders, name='neworders'),
    path('delivered_orders', views.deliveredorders, name='deliveredorders'),
    path('onshipping_orders', views.onshipping, name='onshipping'),
    path('preparing_orders', views.preparing, name='preparing'),
    path('total_orders', views.totalorders, name='totalorders'),
    # path('change password', views.userpassword, name='userpassword'),
    
]