# Generated by Django 5.0.4 on 2024-05-15 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('closed', models.BooleanField(default=False, verbose_name='Закрыто')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
            },
        ),
    ]
