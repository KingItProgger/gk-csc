# Generated by Django 5.0.4 on 2024-04-19 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("csc", "0005_remove_flat_price_for_metr"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="flat",
            options={
                "ordering": ["square"],
                "verbose_name": "квартира",
                "verbose_name_plural": "квартиры",
            },
        ),
        migrations.AlterModelOptions(
            name="house",
            options={
                "ordering": ["year"],
                "verbose_name": "дом",
                "verbose_name_plural": "дома",
            },
        ),
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ["datetime"],
                "verbose_name": "новость",
                "verbose_name_plural": "новости",
            },
        ),
    ]
