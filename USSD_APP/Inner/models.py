from django.contrib.auth.models import AbstractUser
from django.db import models 
import uuid
from django.db.models.constraints import UniqueConstraint 
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

def validate_phone(val):
    if len(str(val)) != 10 :
        raise ValidationError('Phone number too long or too short')
    
def validate_pin(val):
    if len(str(val)) != 4 :
        raise ValidationError('PIN is not ideal length')

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
    age = models.PositiveIntegerField(null=False,blank=False,validators=[MinValueValidator(19)])
    maj_currency = models.CharField(choices=Currencies.choices,null=False,blank=False,max_length=3)
    balance = models.PositiveIntegerField(default=0,null=False)
    phone = models.PositiveBigIntegerField(blank=False,null=False,validators=[validate_phone])
    pin = models.PositiveIntegerField(validators=[validate_pin])  


    
    # def save(self,**kwargs):    
    #     if len(str(self.pin))   < 5 or len(str(self.pin)) > 5:
    #         raise ValidationError('Too short pin or too long ')
    #     super().save(**kwargs)

    def __str__(self):
        return f'{self.code_name} has {self.age} with {self.balance} reached on {self.phone}'

            

    class Meta:
        constraints = [UniqueConstraint(fields=['code_name','phone','pin'],name='No_same_name_and_phone_number_or_pin')

                    ]
    
        


class Transactions(models.Model):
    trans_id = models.UUIDField(null=False,blank=False,primary_key=True,default=uuid.uuid4)
    sender = models.ForeignKey(PrimaryUser,on_delete=models.CASCADE,related_name='sender_info')
    receiver = models.PositiveBigIntegerField(blank=False,null=False,validators=[validate_phone])
    amount = models.PositiveIntegerField(blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def clean(self):
        super().clean()
        if len(str(self.amount)) > 7 :
            raise ValidationError('Too much money')

    def __str__(self):
        return f'{self.trans_id} from {self.sender.code_name} to {self.receiver}'
