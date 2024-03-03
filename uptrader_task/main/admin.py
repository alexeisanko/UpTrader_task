from django.contrib import admin
from . import models


class MenuItemInline(admin.TabularInline):
    model = models.MenuItem


class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)


admin.site.register(models.Menu, MenuAdmin)
