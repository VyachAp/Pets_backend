from board.helpers.serializers import CollectionView
from board.serializers.posts import PostPetsReadOnlySerializer
from board.models import PostPets, PetsImageModel


class PetPostsReadOnlyView(CollectionView):
    http_method_names = ["get", "options"]
    serializer_class = PostPetsReadOnlySerializer
    queryset = PostPets.objects.all()


