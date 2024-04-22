# Generated by Django 5.0.4 on 2024-04-20 20:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medico", "0002_dadosmedicos"),
    ]

    operations = [
        migrations.AddField(
            model_name="dadosmedicos",
            name="foto",
            field=models.ImageField(
                default=django.utils.timezone.now, upload_to="fotos_perfil"
            ),
            preserve_default=False,
        ),
    ]
