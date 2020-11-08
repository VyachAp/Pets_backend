from rest_framework import serializers
from board.models import PostFood, PostHabitat, PostPets
from board.serializers.images import PetsImageReadOnlySerializer


class PostPetsReadOnlySerializer(serializers.ModelSerializer):
    images = PetsImageReadOnlySerializer(many=True, read_only=True)

    class Meta:
        model = PostPets
        fields = '__all__'


class PostFoodReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFood
        fields = '__all__'


class PostHabitatReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHabitat
        fields = '__all__'
