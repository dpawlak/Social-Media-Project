from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from django.contrib import messages

@login_required
def portrait_update_form(request):
    if request.method ==  'POST':
        p_form = PortraitUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.portrait)

        if p_form.is_valid():  
            p_form.save()   
            messages.success(request, f'Your account has been updated!') 
            return redirect('../groups')                  
    else: 
        p_form = PortraitUpdateForm(instance=request.user.portrait)

    context = {
        'p_form': p_form
    }

    return render(request, 'update_portrait.html', context)

