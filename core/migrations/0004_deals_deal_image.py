# Generated by Django 3.2.5 on 2021-07-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210703_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='deals',
            name='deal_image',
            field=models.ImageField(default=False, upload_to='deals/', verbose_name='Фото'),
        ),
    ]
