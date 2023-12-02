from django.contrib import admin
from . models import Update,Award,Bussiness_Sector,Contact,Indexform,Gallery

# Register your models here.

@admin.register(Update)
class Admin(admin.ModelAdmin):
    list_display = ("name" , "user" , "date" , "comment" , "description")



admin.site.register(Award)


admin.site.register(Bussiness_Sector)


@admin.register(Contact)
class Admin(admin.ModelAdmin):
    list_display = ("name" , "email" , "message" )



@admin.register(Indexform)
class Admin(admin.ModelAdmin):
    list_display = ("first_name" , "last_name" , "email" , "message" )



@admin.register(Gallery)
class Admin(admin.ModelAdmin):
    list_display = ("name",)





