from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(verbose_name='Наименование меню', max_length=100, unique=True)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Наименование пункта меню', max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительский пункт меню')

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name
