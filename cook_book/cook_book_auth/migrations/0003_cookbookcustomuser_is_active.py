# Generated by Django 4.0.3 on 2022-04-10 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook_book_auth', '0002_alter_cookbookcustomuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cookbookcustomuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
