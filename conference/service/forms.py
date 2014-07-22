from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    contact_email = forms.EmailField(max_length=254)
    contact_phone = forms.CharField(max_length=20)
