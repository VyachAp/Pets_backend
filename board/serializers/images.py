from rest_framework.serializers import ModelSerializer
from board.models import Images


class ImagesReadOnlySerializer(ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
