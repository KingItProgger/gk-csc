# Generated by Django 5.0.4 on 2024-05-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csc", "0014_room_alter_flat_rooms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="rooms",
            field=models.IntegerField(verbose_name="количество комнат"),
        ),
    ]