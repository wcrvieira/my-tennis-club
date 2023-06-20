from django.db import models

class Member(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    joined_date = models.DateField(null=True)

def __str__(self):
    return f"{self.firstName} {self.lastName}"