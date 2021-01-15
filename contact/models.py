from django.db import models
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(default=0)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email;