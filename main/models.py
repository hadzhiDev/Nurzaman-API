from django.db import models

from django_resized import ResizedImageField


class Object(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название объекта")
    address = models.CharField(max_length=255, verbose_name="Адрес объекта")
    image =  ResizedImageField(size=[800, 600], upload_to='objects/', verbose_name="Изображение объекта",
                               blank=True, null=True, quality=90, crop=['middle', 'center'])
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
    

class Block(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название блока")
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name="blocks", verbose_name="Объект")
    floors_count = models.IntegerField(verbose_name="Количество этажей в блоке")

    def __str__(self):
        return f"Block {self.name} of {self.object.name}"   
    
    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"


class Apartment(models.Model):
    APARTMENT_TIPES = (
        ('studio', 'Студия'),
        ('standard', 'Стандартная'),
        ('commercial', 'Коммерческая'),
        ('penthouse', 'Пентхаус'),
    )
    number = models.IntegerField(verbose_name="Номер квартиры")
    floor = models.IntegerField(verbose_name="Этаж")
    rooms_count = models.IntegerField(verbose_name="Количество комнат")
    area = models.FloatField(verbose_name="Площадь в квадратных метрах")
    image = ResizedImageField(size=[800, 600], upload_to='apartments/', verbose_name="Изображение квартиры",
                              blank=True, null=True, quality=90, crop=['middle', 'center'])
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="apartments", verbose_name="Блок", null=True)
    type = models.CharField(max_length=20, choices=APARTMENT_TIPES, default='standard', verbose_name="Тип квартиры")

    
    def __str__(self):
        return f"Apartment {self.number} on floor {self.floor} with {self.rooms_count} rooms"
    
    class Meta:
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
        unique_together = ('number', 'block')



