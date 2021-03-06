# Generated by Django 3.2.5 on 2021-07-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Значение')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Счетчик',
                'verbose_name_plural': 'Счетчики',
            },
        ),
        migrations.CreateModel(
            name='LiveHelpers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=40, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('middlename', models.CharField(max_length=40, verbose_name='Отчество')),
                ('inst_link', models.URLField(blank=True, verbose_name='Сылка Инстаграм')),
                ('facebook_link', models.URLField(blank=True, verbose_name='Ссылка на Facebook')),
                ('vk_link', models.URLField(blank=True, verbose_name='Ссылка в ВК')),
            ],
            options={
                'verbose_name': 'Участника',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Сканы документов в формате изображений')),
                ('description', models.TextField(verbose_name='Описание изображения')),
                ('testfield', models.TextField()),
            ],
            options={
                'verbose_name': 'Изображение проекта',
                'verbose_name_plural': 'Изображения проекта',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Заголовок', max_length=100, unique=True, verbose_name='Заголовок проекта')),
                ('title_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фотография')),
                ('short_description', models.TextField(default='Краткое описание', max_length=200, verbose_name='Краткое описание')),
                ('full_description', models.TextField(default='Описание', verbose_name='Полное описание')),
                ('collected_money', models.IntegerField(default=0, help_text='Запонять сумму в рублях', verbose_name='Собрано денег')),
                ('need_money', models.IntegerField(default=0, help_text='Заполнять сумму в рублях', verbose_name='Необходимо денег')),
                ('slug', models.CharField(blank=True, help_text='Заполняется автоматически', max_length=160, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=12, null=True, verbose_name='Заголовок страницы')),
                ('logo', models.ImageField(blank=True, upload_to='', verbose_name='Логотип')),
                ('logo_title', models.CharField(blank=True, max_length=120, null=True, verbose_name='Текст логотипа')),
                ('logo_text', models.CharField(blank=True, max_length=200, null=True, verbose_name='Девиз')),
                ('public_offer', models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Договор публичной оферты')),
                ('politics', models.FileField(blank=True, null=True, upload_to='documents/', verbose_name='Политика конфендициальности')),
            ],
            options={
                'verbose_name': 'Настройку',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
