from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username','email', 'password','confirm_password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']

        if password != password2:
            raise serializers.ValidationError({'error':'password and confirm password is not same'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account
