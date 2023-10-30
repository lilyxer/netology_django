from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        request = self.context['request']
        if (request.method == 'POST'                # метода на добавление?
            and data.get('status') == 'OPEN'        # в словаре статус = ОТКРЫТО
            and Advertisement.objects.filter(creator=request.user,      # проверяем сколько открытых сообщений
                                             status='OPEN').count() >= 10):
            raise exceptions.ValidationError('Слишком много открытых объявлений!')
        return data
