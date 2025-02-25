from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Выведем базовую информацию, можно расширить по мере необходимости
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'role')
