from django.db import models
from django.db.models.base import Model
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField

class Settings(models.Model):
    title = models.CharField(verbose_name="Заголовок страницы", max_length=20, null=True, blank=True)
    logo = models.ImageField(verbose_name="Логотип", blank=True)
    logo_title = models.CharField(max_length=120,verbose_name="Текст логотипа", null=True, blank=True)
    logo_text = models.CharField(max_length=200, verbose_name="Девиз", null=True, blank=True)
    public_offer = models.FileField(upload_to='documents/', null=True, verbose_name="Договор публичной оферты", blank=True)
    politics = models.FileField(upload_to='documents/', null=True, verbose_name="Политика конфендициальности", blank=True)
    inst_link = models.URLField(verbose_name="Ссылка на инстаграм", default="https://www.instagram.com/livedream_stav/")

    def __str__(self):
        return "Настройки сайта"

    class Meta:
        verbose_name = "Настройку"
        verbose_name_plural = "Настройки"


class Counters(models.Model):
    count = models.PositiveIntegerField(verbose_name="Значение")
    description = models.CharField(max_length=100, verbose_name="Описание", null=True,)

    def __str__(self):
        return f"{self.count} - {self.description}"

    class Meta:
        verbose_name = "Счетчик"
        verbose_name_plural = "Счетчики"

class ProjectImages(models.Model):
    image = models.ImageField(verbose_name="Сканы документов в формате изображений")
    description = models.TextField("Описание изображения")
    testfield = models.TextField()

    def __str__(self):
        return f"{self.image} - {self.description}"

    class Meta:
        verbose_name = "Изображение проекта"
        verbose_name_plural = "Изображения проекта"

class Projects(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок проекта', unique=True, default="Заголовок")
    title_image = models.ImageField(verbose_name="Фотография", null=True, blank=True)
    short_description = models.TextField(max_length=200, verbose_name="Краткое описание", default="Краткое описание")
    full_description = models.TextField("Полное описание", default="Описание")
    collected_money = models.IntegerField("Собрано денег", help_text="Запонять сумму в рублях", default=0)
    need_money = models.IntegerField("Необходимо денег", help_text="Заполнять сумму в рублях", default=0)

    slug = models.CharField(max_length=160, unique=True, verbose_name="URL", help_text="Заполняется автоматически", blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.collected_money} - {self.need_money}"

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class LiveHelpers(models.Model):
    firstname = models.CharField(max_length=40, verbose_name="Имя")
    lastname = models.CharField(max_length=40, verbose_name="Фамилия")
    middlename = models.CharField(max_length=40, verbose_name="Отчество")
    inst_link = models.URLField(verbose_name="Сылка Инстаграм", blank=True)
    facebook_link = models.URLField(verbose_name="Ссылка на Facebook", blank=True)
    vk_link = models.URLField(verbose_name="Ссылка в ВК", blank=True)

    def __str__(self):
        return f"{self.lastname} - {self.firstname} - {self.middlename}"

    class Meta:
        verbose_name = "Участника"
        verbose_name_plural = "Участники"


class Partners(models.Model):
    partner_title = models.CharField("Название Организации", max_length=50)
    partner_logo = models.ImageField(verbose_name="Логотип партнера")
    partner_link = models.URLField(verbose_name="Ссылка на сайт партнера", blank=True, null=True, help_text="Необязательно")

    def __str__(self):
        return f"{self.partner_title}"


    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


class Deals(models.Model):
    deal_title = models.CharField(verbose_name="Заголовок", max_length=200)
    deal_sort_desc = models.TextField(verbose_name="Краткое описание", max_length=400)
    deal_full_desc = models.TextField(verbose_name="Описание")
    deal_date = models.DateField(verbose_name="Дата организации мероприятия")
    deal_image = models.ImageField(upload_to="deals/", verbose_name="Фото", default=False)


class UserRequests(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)


