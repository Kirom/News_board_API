# Generated by Django 3.1 on 2020-09-01 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0004_auto_20200901_2006"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="author_name",
            field=models.ForeignKey(
                default=4, on_delete=django.db.models.deletion.CASCADE, to="auth.user"
            ),
            preserve_default=False,
        ),
    ]
