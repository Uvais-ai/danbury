from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact,Indexform
from django.forms import widgets

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Your Name"}),
            "email": widgets.EmailInput(attrs={"class": "form-control required email", "placeholder": "Your Email",}),
            "message": widgets.Textarea(attrs={"class": "form-control textarea required", "placeholder": "Your message",}),
        }


class IndexForm(forms.ModelForm):
    
    class Meta:
        model = Indexform
        exclude = ("timestamp",)
        widgets = {
            "first_name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "First Name"}),
            "last_name": widgets.TextInput(attrs={"class": "form-control", "placeholder": "Last Name"}),
            "email": widgets.EmailInput(attrs={"class": "form-control required email","placeholder": "Your Email",}),
            "message": widgets.Textarea(attrs={"class": "form-control textarea required", "placeholder": "Your message",}), 
        }


        
        