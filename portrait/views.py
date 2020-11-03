from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *

def update_portrait_view(request):

    if request.method == 'POST':
        form = UpdatePortraitForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('portrait/success')

    else:
        form = UpdatePortraitForm()
    return render(request, 'picture.html', {'form' : form})

def success(request):
    return HttpResponse('successfully updated')
