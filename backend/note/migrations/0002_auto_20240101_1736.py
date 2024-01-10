# Generated by Django 3.2.23 on 2024-01-01 14:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_trash',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0a70769c-a25a-4705-8ea3-f1c296848c2b'), primary_key=True, serialize=False, unique=True),
        ),
    ]
