from django.db import models
from django.utils.text import slugify

# Create your models here.


class Menu(models.Model):
    name = models.CharField(verbose_name='Наименование меню', max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    name = models.CharField(verbose_name='Наименование пункта меню', max_length=100)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Родительский пункт меню')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'


