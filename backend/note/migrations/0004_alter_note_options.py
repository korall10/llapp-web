# Generated by Django 3.2.23 on 2024-01-09 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20240101_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created_at']},
        ),
    ]
