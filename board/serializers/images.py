from rest_framework.serializers import ModelSerializer
from board.models import ImagesPost


class ImagesReadOnlySerializer(ModelSerializer):
    class Meta:
        model = ImagesPost
        fields = '__all__'
