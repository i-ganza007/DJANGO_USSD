from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.db.models import Q
from django.db.models.constraints import UniqueConstraint , CheckConstraint

# Creating the USER model 
class PrimaryUser(AbstractUser):
    class Currencies(models.TextChoices):
        rwf = ('RWF','RWF')
        usd = ('USD','USD')
        ugx = ('UGX','UGX')
        ksh = ('KSH','KSH')
        eur = ('EUR','EUR')

    id= models.AutoField(primary_key=True,null=False,blank=False)
    code_name = models.CharField(max_length=10,null=False,blank=False,unique=True)
    age = models.PositiveIntegerField(null=False,blank=False)
    maj_currency = models.CharField(choices=Currencies,null=False,blank=False)
    balance = models.PositiveIntegerField(default=0,null=False)
    phone = models.PositiveBigIntegerField(max_length=10,blank=False,null=False)

    class Meta:
        constraints = [UniqueConstraint(fields=['code_name','phone'],name='No_same_name_and_phone_number'),
                       CheckConstraint(check=Q(age_gte = 18) and (age_lte = 80))
                       ]

class Transactions(models.Model):
    id= models.AutoField()
    trans_id = models.UUIDField(null=False,blank=False,primary_key=True)
    sender = models.ForeignKey(PrimaryUser,on_delete=CASCADE,related_name='sender')
    receiver = models.PositiveBigIntegerField(max_length=10,blank=False,null=False)
    amount = models.PositiveIntegerField(max_length=7,blank=False,null=False)
