from django.db import models


class Car(models.Model):
    CHOICE_NEW_OR_USED = (
        ('new', 'Новый'),
        ('used', 'Б/у'),
    )

    name = models.CharField("Название", max_length=10)
    marka = models.CharField("Марка", max_length=10)
    manufacturer = models.CharField("Компанию", max_length=100, null=True, blank=True)
    model = models.CharField("Модель", max_length=50, null=True, blank=True)
    body_type = models.CharField("Кузов", max_length=40, default=0, null=True, blank=True)
    ingine_size = models.FloatField("Объем", null=True, blank=True)
    vin_code = models.IntegerField("VIN код", null=True, blank=True)
    condition = models.CharField("Состояние", max_length=10, choices=CHOICE_NEW_OR_USED, default='new', null=True, blank=True)
    license_plate = models.CharField("Гос номер", max_length=10, null=True, blank=True)
    in_stock = models.BooleanField('В наличии', default=False)
    on_sale = models.BooleanField('В продаже', default=False)
    sold = models.BooleanField('Продано', default=False)
    image_car = models.ImageField("Фото", null=True, blank=True)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class Person(models.Model):
    surname = models.CharField("Фамилия", max_length=100)
    name = models.CharField("Имя", max_length=100)
    age = models.IntegerField("Возраст", help_text='возраст')

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"


class Application(models.Model):
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField("Имя",max_length=100)
    age = models.IntegerField("Возраст", blank=True)
    car = models.CharField("Машина", max_length=75)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"