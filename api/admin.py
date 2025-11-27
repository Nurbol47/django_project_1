from django.contrib import admin
from django.utils.html import format_html

from .models import Car, Person, Application


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    model = Car
    list_display = ['name', "model", "marka", 'in_stock', 'on_sale', 'sold', 'image_preview']

    def image_preview(self, obj):
        if obj.image_car:
            return format_html(
                '<img src="{}" style="width:50px; height: 50px;" />',
                obj.image_car.url
            )
        return 'Нет фото'

    image_preview.short_description = "Превью"


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    people = Person
    list_display = ["surname", 'name', 'age']
    list_filter = ('surname', 'name', 'age')
    search_fields = ['surname', 'name', 'age']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    application = Application
    list_display = ['surname', 'name', 'age', 'car']
    list_filter = ("surname", 'name', 'age', 'car')
    search_fields = ['surname', 'name', 'car']
