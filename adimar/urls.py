
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_view
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('signup/', user_view.signup, name='user-signup'),
    path('logout/', auth_view.LogoutView.as_view(), name='user-logout'),
    path('products/', include('products.urls', namespace= 'products')),
    path('payments/', include('payments.urls', namespace='payments')),
    path('user/', include('user.urls', namespace='user')),
    path('order/', include('order.urls', namespace='order')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)