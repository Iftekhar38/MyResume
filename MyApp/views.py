from django.shortcuts import render
from .import forms
# Create your views here.
def index(request):
    form = forms.ContactForm
    if request.method=='POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
       
    return render(request, 'MyApp/index.html', {'form':form})