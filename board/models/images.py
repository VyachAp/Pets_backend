from django.db import models
from board.models.posts import Post
import uuid
from board.helpers.images import get_upload_path


class ImagesPost(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    url = models.FileField(upload_to=get_upload_path, null=True)
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name='Порядок в объявлении', default=1)

    class Meta:
        app_label = "board"

        verbose_name = "Фотография объявления животных"
        verbose_name_plural = "Фотографии объявления животных"
        db_table = "images_post"

    def __str__(self):
        return f"PostPets {self.pk}: {self.title} - {self.created_at}"

