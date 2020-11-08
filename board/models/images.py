from django.db import models
from board.models.posts import PostPets, PostHabitat, PostFood
import uuid
from board.helpers.images import get_upload_path


class PetsImageModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    mainimage = models.FileField(upload_to=get_upload_path, null=True)
    post = models.ForeignKey(PostPets, related_name='images', on_delete=models.CASCADE)
    order = models.IntegerField(verbose_name='Порядок в объявлении', default=1)

    class Meta:
        app_label = "board"

        verbose_name = "Фотография объявления животных"
        verbose_name_plural = "Фотографии объявления животных"
        db_table = "pets_images"

    def __str__(self):
        return f"PostPets {self.pk}: {self.title} - {self.created_at}"


class HabitatImageModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    mainimage = models.FileField(upload_to='images', null=True)
    post = models.ForeignKey(PostHabitat, related_name='image', on_delete=models.CASCADE)


class FoodImageModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    mainimage = models.FileField(upload_to='images', null=True)
    post = models.ForeignKey(PostFood, related_name='image', on_delete=models.CASCADE)
