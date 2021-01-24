from rest_framework import serializers
from board.models import Post
from board.serializers.images import ImagesReadOnlySerializer


class PostReadOnlySerializer(serializers.ModelSerializer):
    images = ImagesReadOnlySerializer(many=True, read_only=True)
    subcategory = serializers.CharField(source='subcategory.name')

    def get_images(self, post):
        return post.images.values_list('mainimage', flat=True)

    class Meta:
        model = Post
        fields = '__all__'
