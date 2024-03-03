from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.http import HttpResponseNotFound

from main.models import MenuItem, Menu


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context


def show_menu(request, select_submenu):
    try:
        selected = select_submenu.split('/')
        menu_name = selected[0]
        menu_item = None if len(selected) == 1 else selected[-1]
    except IndexError:
        return HttpResponseNotFound("<h1>I am sorry...</h1>")

    return render(
        request, 'index.html', {'selected_menu': menu_name, 'menu_item': menu_item})
