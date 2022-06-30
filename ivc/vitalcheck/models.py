from django.db import models

# Create your models here.

# name,photo,height,bodytemp,pulse

class UserData(models.Model):

    name = models.CharField(max_length=30,blank=False,null=False)
    height = models.PositiveIntegerField()
    bodytemp = models.PositiveSmallIntegerField()
    pulse = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class UserImage(models.Model):
    profile_pic = models.ImageField(upload_to='images')
    user = models.OneToOneField(UserData,on_delete=models.CASCADE,related_name='image')


    def __str__(self):
        return self.user.name

