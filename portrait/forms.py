from django import forms
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
class UpdatePortraitForm(forms.ModelForm):
    class Meta:
        model = Portrait
        fields = ['image', 'user']