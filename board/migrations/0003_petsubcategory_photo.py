# Generated by Django 3.1.2 on 2021-03-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='petsubcategory',
            name='photo',
            field=models.ImageField(default=1, upload_to='None_category/'),
            preserve_default=False,
        ),
    ]
