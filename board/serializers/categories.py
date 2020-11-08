from rest_framework.serializers import ModelSerializer
from board.models import PetCategory, PetSubcategory


class PetCategoryReadOnlySerializer(ModelSerializer):
    class Meta:
        model = PetCategory
        fields = ("id", "name")


class PetSubcategoryReadOnlySerializer(ModelSerializer):
    category = PetCategoryReadOnlySerializer(source='pet_category.name', read_only=True)

    class Meta:
        model = PetSubcategory
        fields = ("name", "category",)
