from django.db import models

# Create your models here.

class query(models.Model):
    name = models.CharField(max_length=200,blank=False)
    email = models.EmailField(max_length=200,blank=False)
    subject = models.CharField(max_length=200,blank=False)
    message = models.TextField(blank=False)
    def __str__(self):
        return self.subject
