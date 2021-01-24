from rest_framework import serializers
from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'phone', 'username', 'email', 'last_login', 'is_active', 'date_joined']
        read_only_fields = ('last_login', 'is_active', 'date_joined')


class AccountLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['phone']


class AccountVerifySerializer(serializers.ModelSerializer):
    code = serializers.IntegerField()

    class Meta:
        model = Account
        fields = ['phone', 'code']
