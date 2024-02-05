from django.db import models

from django.conf import settings


class MenuItem(models.Model):
    """Модель меню и пунктов меню."""
    name = models.CharField(
        'Наименование меню/пунктов меню', max_length=settings.MAX_LENGTH_NAME
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True,
        blank=True, related_name='children'
    )
    url = models.CharField(
        'Идентификатор URL', max_length=settings.MAX_LENGTH_URL
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return self.name[:settings.MAX_NAME]
