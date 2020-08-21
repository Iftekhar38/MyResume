from django.contrib import admin
from MyApp.models import Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Contact, ContactAdmin)
