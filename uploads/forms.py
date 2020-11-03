from django import forms
from .models import *

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile_Pic
        fields = ['name', 'profile_Main_Img']

    