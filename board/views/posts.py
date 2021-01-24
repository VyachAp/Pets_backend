from board.helpers._views import CollectionView, SingleObjectsView
from board.serializers.posts import PostReadOnlySerializer
from board.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostsView(CollectionView):
    serializer_get = PostReadOnlySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()


class PostView(SingleObjectsView):
    serializer_get = PostReadOnlySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
