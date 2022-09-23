from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    second_name = models.CharField(max_length=255, blank=False, null=False)
    is_vendor = models.BooleanField(default=False, null=False, blank=True)

    def __str__(self):
        return f'{self.user}'