# Generated by Django 3.0.6 on 2020-05-07 14:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200505_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='date',
        ),
        migrations.AddField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]