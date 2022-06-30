from django.contrib import admin
from vitalcheck.models import UserData, UserImage
# Register your models here.

class UserDataAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserData,UserDataAdmin)



class UserImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserImage,UserImageAdmin)

