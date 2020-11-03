from django.db import models

class Profile_Pic(models.Model):
    name = models.CharField(max_length=50)
    profile_Main_Img = models.ImageField(upload_to='images/')

    