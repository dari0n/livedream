# Generated by Django 3.2.5 on 2021-07-03 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_deals_deal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Заголовок страницы'),
        ),
    ]
