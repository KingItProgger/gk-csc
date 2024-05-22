# Generated by Django 5.0.4 on 2024-05-15 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("csc", "0015_alter_flat_rooms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flat",
            name="rooms",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="csc.room",
                verbose_name="количество комнат",
            ),
        ),
    ]