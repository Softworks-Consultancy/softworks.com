from django.db import models

class ContactRequest(models.Model):

    name = models.CharField(max_length=455)
    email = models.EmailField()
    phone = models.CharField(max_length=30, null=True, blank=True)
    servicetype = models.CharField(max_length=100)
    message = models.TextField()

