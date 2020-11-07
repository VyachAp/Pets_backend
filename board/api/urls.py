from board.views import PetCategoriesView, PetSubcategoriesView
from django.urls import path

app_name = "api-v1"


urlpatterns = [
    path("categories/", PetCategoriesView.as_view(), name="categories"),
    path(
        "categories/<str:category_number>/",
        PetSubcategoriesView.as_view(),
        name="subcategories",
    )]