# Generated by Django 3.1.1 on 2021-02-27 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system', '0003_auto_20210227_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='borrower',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='book_borrower', to=settings.AUTH_USER_MODEL),
        ),
    ]
