from django import template
from django.core.exceptions import ObjectDoesNotExist

from main.models import MenuItem

register = template.Library()


@register.inclusion_tag("menu.html")
def draw_menu(menu: str = None, item_menu: str = None) -> dict:
    def get_menu(item_menu: str = None, submenu: list = None) -> list:
        if item_menu is None:
            menu = list(items.filter(parent=None))
        else:
            menu = list(items.filter(parent__slug=item_menu))
        try:
            menu.insert(menu.index(submenu[0].parent) + 1, submenu)
        except (IndexError, TypeError):
            pass
        try:
            return get_menu(items.get(slug=item_menu).parent.slug, menu)
        except ObjectDoesNotExist:
            return menu
        except AttributeError:
            return get_menu(submenu=menu)

    items = MenuItem.objects.filter(menu__slug=menu)
    return {'menu': get_menu(item_menu)}
