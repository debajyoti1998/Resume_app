from django.db import models

STATE_CHOICE=(
    ('channi','channi'),
    ('west bengal','west bengal'),
    ('gujrat','gujrat'),
    ('mumbai','mumbai')
)


class Resume(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    DOB=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    state=models.CharField(choices=STATE_CHOICE,max_length=50)
    city=models.CharField(max_length=100)
    gender=models.CharField(max_length=12)
    profile_image=models.ImageField(upload_to="pics/products/",default='')

    
