from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
from uploads import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ 
    path('image_upload', profile_image_view, name = 'image_upload'), 
    path('uploads/success', views.success, name = 'success'), 
    path('uploads/profile_images', views.display_profile_images, name = 'profile_images'),
] 

