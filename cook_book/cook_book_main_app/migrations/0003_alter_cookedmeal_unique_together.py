# Generated by Django 4.0.3 on 2022-04-10 20:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cook_book_main_app', '0002_alter_mealimage_image'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cookedmeal',
            unique_together={('type', 'title', 'ingredients', 'cooking_time', 'description', 'user')},
        ),
    ]
