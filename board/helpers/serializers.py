from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.filters import OrderingFilter

from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)


class CollectionView(
    CreateModelMixin, ListModelMixin, GenericAPIView,
):
    queryset = None
    serializer_class = None

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_class = None
    filterset_fields = []
    ordering_fields = []
    ordering = []

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def create(self, request, *args, **kwargs):
        data = self.get_request_data()
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def get_request_data(self):
        data = self.request.data
        if not isinstance(data, list):
            data = [data]
        return data

    def get_serializer_class(self):
        return getattr(
            self, f"serializer_{self.request.method.lower()}", self.serializer_class
        )

    def get_permissions(self):
        permissions = getattr(
            self,
            f"permission_classes_{self.request.method.lower()}",
            self.permission_classes,
        )
        return [permission() for permission in permissions]


class SingleObjectsView(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView,
):
    queryset = None
    serializer_class = None

    filter_class = None
    filterset_fields = []

    def get(self, request, pk):
        return self.retrieve(request)

    def patch(self, request, pk):
        return self.partial_update(request)

    def delete(self, request, pk):
        return self.destroy(request)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        data = self.get_request_data()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def get_request_data(self):
        return self.request.data

    def get_serializer_class(self):
        return getattr(
            self, f"serializer_{self.request.method.lower()}", self.serializer_class
        )

    def get_permissions(self):
        permissions = getattr(
            self,
            f"permission_classes_{self.request.method.lower()}",
            self.permission_classes,
        )
        return [permission() for permission in permissions]
