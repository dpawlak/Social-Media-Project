from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
from uploads import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [ 
    path('portrait_update', portrait_update_form, name = 'portrait_update'), 
    path('portrait/success', views.success, name = 'success'), 
]

