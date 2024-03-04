import random

from django.core.management.base import BaseCommand

from main.models import Menu, MenuItem


class Command(BaseCommand):
    help = 'Load simple data for test application'

    def handle(self, *args, **options):
        count_menu = 4

        for number_menu in range(1, count_menu + 1):
            new_menu = Menu.objects.create(name=f'Menu #{number_menu}')

            def _create_items_child(parent=None, menu=None):
                count_item = random.randint(0, 2)
                for number_item in range(1, count_item + 1):
                    if parent is None:
                        new_item = MenuItem.objects.create(name=f'{menu} > Item #{number_item}', menu=new_menu)
                    else:
                        new_item = MenuItem.objects.create(name=f'{parent} > Item #{number_item}', menu=new_menu, parent=parent)
                    _create_items_child(parent=new_item, menu=new_menu)

            _create_items_child(menu=new_menu)

        self.stdout.write(self.style.SUCCESS('БД для просмотра примера заполнена'))
