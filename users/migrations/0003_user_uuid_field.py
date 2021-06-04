# Generated by Django 3.0.5 on 2021-06-04 16:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210604_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uuid_field',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
