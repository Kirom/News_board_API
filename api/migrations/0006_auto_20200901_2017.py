# Generated by Django 3.1 on 2020-09-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_auto_20200901_2013"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="amount_of_upvotes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
