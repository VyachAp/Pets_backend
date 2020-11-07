from django.db import models


class PetCategory(models.Model):
    objects = models.Manager()

    name = models.CharField("Название категории", max_length=200, unique=True)

    class Meta:
        app_label = "board"

        verbose_name = "Категория животных"
        verbose_name_plural = "Категории животных"
        db_table = "pet_category"

    def __str__(self):
        return f"{self.pk}: {self.name}"


class PetSubcategory(models.Model):
    objects = models.Manager()

    name = models.CharField("Название подкатегории", max_length=200, unique=True)
    category = models.ForeignKey(PetCategory, verbose_name='Категория', on_delete=models.CASCADE, related_name="pet_subcategory")

    class Meta:
        app_label = "board"

        verbose_name = "Подкатегория животных"
        verbose_name_plural = "Подкатегории животных"
        db_table = "pet_subcategory"

    def __str__(self):
        return f"{self.pk}: {self.name}"
