# Generated by Django 3.1.2 on 2020-11-07 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория животных',
                'verbose_name_plural': 'Категории животных',
                'db_table': 'pet_category',
            },
        ),
        migrations.CreateModel(
            name='PetSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Название подкатегории')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_subcategory', to='board.petcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория животных',
                'verbose_name_plural': 'Подкатегории животных',
                'db_table': 'pet_subcategory',
            },
        ),
    ]