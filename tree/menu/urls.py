from django.urls import path

from .views import MenuListView

app_name = 'menu'


urlpatterns = [
    path('<str:menu_name>/', MenuListView.as_view(), name='display_menu'),
]
