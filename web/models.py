from django.db import models

# Create your models here.

class Update(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100) 
    user = models.CharField(max_length=100)
    date = models.DateField()
    comment = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
    

class Award(models.Model):
    name = models.CharField(max_length=100)
    ICON_CHOICES = (
        ('flaticon-heart', 'Heart Icon'), 
        ('flaticon-yoga', 'Yoga Icon'),
        ('flaticon-sneakers', 'Sneakers Icon'),
    )
    spanclassname = models.CharField(max_length=20, choices=ICON_CHOICES)

    def __str__(self):
        return self.name 
    

    
class Bussiness_Sector(models.Model):
    name = models.CharField(max_length=100)
    ICON_CHOICES = (
        ('flaticon-heart', 'Heart Icon'), 
        ('flaticon-yoga', 'Yoga Icon'),
        ('flaticon-sneakers', 'Sneakers Icon'),
    )
    spanclassname = models.CharField(max_length=20, choices=ICON_CHOICES)

    def __str__(self):
        return self.name
    


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
 


class Indexform(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.first_name)
    


class Gallery(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to = "img_branches")

    def __str__(self):
        return self.name
    
    
    

    
    

    



    