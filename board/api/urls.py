from board.views import PetCategoriesView, PetSubcategoriesView, PostsView
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings

app_name = "api_v1"

urlpatterns = [
    path("categories/", PetCategoriesView.as_view(), name="categories"),
    path(
        "categories/<str:category_number>/",
        PetSubcategoriesView.as_view(),
        name="subcategories",
    ),
    path("posts/", PostsView.as_view(), name='posts')]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(title="Pets API", default_version="v1"),
        public=True,
        permission_classes=(permissions.AllowAny,),
        authentication_classes=(),
    )

    urlpatterns = [
        re_path(
            r"^swagger(?P<format>\.json|\.yaml)$",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
        ),
    ] + urlpatterns
