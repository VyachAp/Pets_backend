from django.db import models
from datetime import datetime


class Post(models.Model):
    objects = models.Manager()

    user = models.ForeignKey('accounts.Account', verbose_name="Автор объявления", on_delete=models.CASCADE,
                             related_name='posts_pets')
    description = models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    title = models.CharField("Название объявления", max_length=200)
    category = models.ForeignKey('board.PetCategory', verbose_name='Категория объявления',
                                 on_delete=models.CASCADE, related_name='category_post')
    subcategory = models.ForeignKey('board.PetSubcategory', verbose_name='Подкатегория объявления',
                                    on_delete=models.CASCADE, related_name='subcategory_post')
    year_of_birth = models.IntegerField(verbose_name='Год рождения', null=True)
    month_of_birth = models.IntegerField(verbose_name='Месяц рождения', null=True)
    day_of_birth = models.IntegerField(verbose_name='День рождения', null=True)
    creation_date = models.DateTimeField(verbose_name='Дата и время создания объявления', default=datetime.now)
    update_date = models.DateTimeField(verbose_name='Дата и время обновления объявления', default=datetime.now)

    class Meta:
        app_label = "board"

        verbose_name = "Объявление о животном"
        verbose_name_plural = "Объявления о животных"
        db_table = "post"

    def __str__(self):
        return f"Post {self.pk}: {self.title} - {self.creation_date}"
