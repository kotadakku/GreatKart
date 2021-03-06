# Generated by Django 3.1.2 on 2021-11-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Mô tả')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')),
                ('images', models.ImageField(upload_to='photos/products', verbose_name='Ảnh')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
