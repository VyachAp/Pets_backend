from rest_framework import serializers
from accounts.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        account = Account(email=self.validated_data['email'],
                          username=self.validated_data['username'],
                          )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли должны совпадать.'})
        account.set_password(password)
        account.save()
        return account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'last_login', 'is_active', 'date_joined', 'password']
        read_only_fields = ('last_login', 'is_active', 'date_joined')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'username': {'required': True}
        }