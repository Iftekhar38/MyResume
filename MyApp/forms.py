from django import forms
from MyApp.models import Contact

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("__all__")
