# Generated by Django 4.0.3 on 2022-04-10 20:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cook_book_main_app', '0003_alter_cookedmeal_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cookedmeal',
            unique_together={('type', 'title', 'user')},
        ),
    ]
