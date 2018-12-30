from django.db import models

# Create your models here.
class Distro(models.Model):
    url = models.URLField(null=True)
    description = models.TextField(null=True, blank=True)
    workspace_url = models.URLField(max_length=100)
    workspace_id = models.IntegerField()

class Contact(models.Model):
    """Podio Contact Model."""

    app_id = models.IntegerField()
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

    def __str__(self):
        """Unicode representation of Contact."""
        pass

class Lead(models.Model):
    """Keep track of potential customers and leave comments about conversations.
        Use the Follow Up buttons to easily create tasks that get added to your calendar."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Lead."""

        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        """Unicode representation of Lead."""
        pass

class Account(models.Model):
    """This app keeps track of all your customer info. Easily create new orders or quotes from the account page using the "new order" and "new quote" buttons.."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Account."""

        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        """Unicode representation of Accounts."""
        pass
