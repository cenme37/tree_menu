from django.views.generic import ListView

from django.conf import settings
from .models import MenuItem


class MenuListView(ListView):
    """Класс для представления страницы меню."""
    model = MenuItem
    template_name = 'menu/index.html'
    context_object_name = 'menu_items'
    paginate_by = settings.MAX_PAGINATE

    def get_queryset(self):
        return super().get_queryset().filter(
            name=self.kwargs['menu_name']
        ).select_related('parent')
