from django.db import models

# Create your models here.
class Distro(models.Model):
    url = models.URLField(null=True)
    description = models.TextField(null=True, blank=True)
    workspace_url = models.URLField(null=True, max_length=100)
    workspace_id = models.IntegerField(null=True)

class Contact(models.Model):
    """Podio Contact Model."""

    app_id = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(blank=True)
    photo =  models.ImageField()
    address = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    date_of_birth = models.DateField()
    notes = models.TextField(max_length=400)
    last_date = models.DateField()

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

