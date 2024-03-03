from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<path:select_submenu>/", views.show_menu, name="show_menu"),
]
