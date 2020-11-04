from django import forms
from .models import *
from django.contrib.auth.decorators import login_required

class PortraitUpdateForm(forms.ModelForm):
    class Meta:
        model = Portrait
        fields = ['image']