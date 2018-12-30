from django.contrib import admin

# Register your models here.
from distro.models import Distro, Contact

admin.site.register(Distro)

admin.site.register(Contact)
