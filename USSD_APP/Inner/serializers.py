from rest_framework import serializers 
from models import PrimaryUser , Transactions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimaryUser
        fields = '__all__'
    def validate_phone(self,val):
        if len(str(val['phone'])) != 9 :
            raise serializers.ValidationError('Phone number too long or too short or remove the leading 0')
        
    def validate_pin(self,val):
        if len(str(val['pin'])) != 4 :
            raise serializers.ValidationError('PIN is not ideal length')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'