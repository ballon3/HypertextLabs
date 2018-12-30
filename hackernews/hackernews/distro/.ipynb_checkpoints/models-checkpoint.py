from django.db import models

# Create your models here.
class Distro(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    
    def str(self):
        return self.url