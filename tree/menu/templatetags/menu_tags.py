from django import template
from django.utils.safestring import mark_safe

from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    """Пользовательский тег шаблона вложенного меню."""
    menu_items = MenuItem.objects.filter(
        name=menu_name
    ).select_related('parent')
    return mark_safe(_render_menu(menu_items))


def _render_menu(menu_items):
    """Преобразовать полученные данные в HTML-шаблон вложенного списка."""
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>'
        if item.url:
            menu_html += f'<a href="{item.url}">{item.name}</a>'
        elif item.named_url:
            menu_html += f'<a href="{item.named_url}">{item.name}</a>'
        else:
            menu_html += item.name
        if item.children.exists():
            menu_html += _render_menu(item.children.all())
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html
