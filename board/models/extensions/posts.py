from board.models.images import PetsImageModel


def get_images(post):
    images = PetsImageModel.objects.filter(post=post.id)
    if images:
        return images
    else:
        return []
