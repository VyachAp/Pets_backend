from board.helpers.serializers import CollectionView
from board.serializers.categories import PetCategoryReadOnlySerializer, PetSubcategoryReadOnlySerializer
from board.models import PetCategory, PetSubcategory
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


class PetCategoriesView(CollectionView):
    http_method_names = ["get", "options"]
    serializer_class = PetCategoryReadOnlySerializer
    queryset = PetCategory.objects.all()


class PetSubcategoriesView(ListAPIView):
    serializer_class = PetSubcategoryReadOnlySerializer
    queryset = PetSubcategory.objects.all()

    def get(self, request, *args, **kwargs):
        category_number = kwargs.get('category_number')
        queryset = self.queryset.filter(category=category_number)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
