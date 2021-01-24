from board.helpers.serializers import CollectionView
from board.serializers.posts import PostReadOnlySerializer
from board.models import Post, Images


class PetPostsReadOnlyView(CollectionView):
    http_method_names = ["get", "options"]
    serializer_class = PostReadOnlySerializer
    queryset = Post.objects.all()


