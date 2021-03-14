from board.helpers._views import CollectionView, SingleObjectsView
from board.serializers.posts import PostReadOnlySerializer
from board.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostsView(CollectionView):
    serializer_get = PostReadOnlySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        """
        Получить список объявлений
        """
        return super(PostsView, self).get(request)

    def post(self, request, *args, **kwargs):
        """
        Создать объявление
        """
        return super(PostsView, self).post(request)


class PostView(SingleObjectsView):
    serializer_get = PostReadOnlySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def get(self, request, pk):
        """
        Получить объявление по id
        """
        return super(PostView, self).get(request, pk)

    def patch(self, request, pk):
        """
        Частично изменить объявление по id
        """
        return super(PostView, self).patch(request, pk)
    
    def delete(self, request, pk):
        """
        Удалить объявление по id
        """
        return super(PostView, self).delete(request, pk)