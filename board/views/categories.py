from board.helpers._views import CollectionView
from board.serializers.categories import PetCategoryReadOnlySerializer, PetSubcategoryReadOnlySerializer
from board.models import PetCategory, PetSubcategory
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from drf_yasg.inspectors import SwaggerAutoSchema


class PetCategoriesView(CollectionView):
    http_method_names = ["get", "options"]
    serializer_class = PetCategoryReadOnlySerializer
    swagger_schema = SwaggerAutoSchema
    queryset = PetCategory.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Получение категорий животных
        """
        return super(PetCategoriesView, self).get(request, *args, **kwargs)


class PetSubcategoriesView(ListAPIView):
    serializer_class = PetSubcategoryReadOnlySerializer
    queryset = PetSubcategory.objects.all()
    swagger_schema = SwaggerAutoSchema

    def get(self, request, *args, **kwargs):
        """
        Получение подкатегорий по номеру категории животного (category_number)
        """
        category_number = kwargs.get('category_number')
        queryset = self.queryset.filter(category=category_number)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
