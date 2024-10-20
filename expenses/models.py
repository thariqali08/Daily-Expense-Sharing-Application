from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100) #User name
    email = models.EmailField(unique=True) #User email
    mobile = models.CharField(max_length=15) #User mobile number

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=255) #description about buy a things or others
    amount = models.DecimalField(max_digits=10, decimal_places=2) #Total amount to paid
    payer = models.ForeignKey(User, related_name='paid_expenses', on_delete=models.CASCADE) #Which user to paid
    participants = models.ManyToManyField(User, related_name='shared_expenses') # Mention to how many participantes to go
    split_method = models.CharField(max_length=10)  # Select option on 'equal', 'exact', 'percentage'
    split_details=models.JSONField(null=True,blank=True) # Mention a amount each user

    def __str__(self):
        return self.description
