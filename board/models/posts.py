from django.db import models
from datetime import datetime


class PostPets(models.Model):
    objects = models.Manager()

    user = models.ForeignKey('accounts.Account', verbose_name="Автор объявления", on_delete=models.CASCADE,
                             related_name='posts_pets')
    description = models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    title = models.CharField("Название объявления", max_length=200)
    subcategory = models.ForeignKey('board.PetSubcategory', verbose_name='Подкатегория объявления',
                                    on_delete=models.CASCADE)
    year_of_birth = models.IntegerField(verbose_name='Год рождения', null=True)
    month_of_birth = models.IntegerField(verbose_name='Месяц рождения', null=True)
    day_of_birth = models.IntegerField(verbose_name='День рождения', null=True)
    creation_date = models.DateTimeField(verbose_name='Дата и время создания объявления', default=datetime.now)
    update_date = models.DateTimeField(verbose_name='Дата и время обновления объявления', default=datetime.now)

    class Meta:
        app_label = "board"

        verbose_name = "Объявление о животном"
        verbose_name_plural = "Объявления о животных"
        db_table = "post_pets"

    def __str__(self):
        return f"PostPets {self.pk}: {self.title} - {self.creation_date}"


class PostHabitat(models.Model):
    objects = models.Manager()

    user = models.ForeignKey('accounts.Account', verbose_name="Автор объявления", on_delete=models.CASCADE,
                             related_name='posts_habitats')
    description = models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    title = models.CharField("Название объявления", max_length=200)
    for_pet = models.ForeignKey('board.PetSubcategory', verbose_name='Для животного',
                                on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='Дата и время создания объявления', default=datetime.now)
    update_date = models.DateTimeField(verbose_name='Дата и время обновления объявления', default=datetime.now)

    class Meta:
        app_label = "board"

        verbose_name = "Объявление о хабитате"
        verbose_name_plural = "Объявления о хабитатах"
        db_table = "post_habitat"

    def __str__(self):
        return f"PostHabitat {self.pk}: {self.title} - {self.creation_date}"


class PostFood(models.Model):
    objects = models.Manager()

    user = models.ForeignKey('accounts.Account', verbose_name="Автор объявления", on_delete=models.CASCADE,
                             related_name='posts_food')
    description = models.TextField("Описание", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    title = models.CharField("Название объявления", max_length=200)
    for_pet = models.ForeignKey('board.PetSubcategory', verbose_name='Для животного',
                                on_delete=models.CASCADE)
    creation_date = models.DateTimeField(verbose_name='Дата и время создания объявления', default=datetime.now)
    update_date = models.DateTimeField(verbose_name='Дата и время обновления объявления', default=datetime.now)

    class Meta:
        app_label = "board"

        verbose_name = "Объявление о еде"
        verbose_name_plural = "Объявления о еде"
        db_table = "post_food"

    def __str__(self):
        return f"PostFood {self.pk}: {self.title} - {self.creation_date}"
