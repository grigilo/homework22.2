# Generated by Django 5.0.4 on 2024-05-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_release_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='release_content',
            field=models.TextField(blank=True, null=True, verbose_name='содержимое'),
        ),
    ]
