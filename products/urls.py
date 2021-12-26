from django.urls import path
from . import views 

app_name = 'products'

urlpatterns = [
    path('', views.content, name='products-content'),
    path('product-detail/<str:id>', views.detail, name='products-detail'),
    path('product-bulkdetail/<str:id>', views.bulk, name='products-bulk'),
    path('all-products/', views.products, name= 'product-products'),
    path('categories/<str:id>/<slug:slug>', views.mcat, name='products-mcat'),
    path('gallery/', views.gallery, name='products-gallery'),
    path('customized/', views.customized, name='products-custom'),
    path('filter/<str:id>', views.filt, name='products-filter'),
    path('product-gallery-detail/<str:id>', views.gallerydet, name='products-gallerydet'),
    # path('send', views.send, name='send'),
    path('loveit', views.loveit, name='loveit')
]
