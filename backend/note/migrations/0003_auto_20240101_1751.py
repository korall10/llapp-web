# Generated by Django 3.2.23 on 2024-01-01 14:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20240101_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
