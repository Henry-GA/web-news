# Generated by Django 3.0.6 on 2020-05-07 17:13

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20200507_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
