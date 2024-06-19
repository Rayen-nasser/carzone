from datetime import datetime

from django.db import models

class Contact(models.Model):
    car_id = models.IntegerField()
    user_id = models.IntegerField()
    car_title = models.CharField(max_length=255)
    customer_need = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
