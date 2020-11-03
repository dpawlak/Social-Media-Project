from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
  

def profile_image_view(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('uploads/success')

    else:
        form = ProfileForm()
    return render(request, 'picture.html', {'form' : form})

def success(request):
    return HttpResponse('successfully uploaded')


def display_profile_images(request):

    if request.method == 'GET':

        Profile_Pics = Profile_Pic.objects.all()
        return render(request, 'display_profile_images.html', 
                        {'profile_images': Profile_Pics})


