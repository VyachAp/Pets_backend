from rest_framework.serializers import ModelSerializer
from board.models import PetsImageModel


class PetsImageReadOnlySerializer(ModelSerializer):
    class Meta:
        model = PetsImageModel
        fields = ('mainimage',)
