import csv
import os

import django.db.utils
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from menu.models import MenuItem

DATA_CSV = {
    MenuItem: 'menu.csv'
}


def read_csv(name_file):
    """Считывает данные из csv-файлов."""
    path = os.path.join('static/data', name_file)
    with open(path, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        return list(reader)


def get_list_fields_model(model):
    """Принимает объект модели, и возвращает словарь с полями."""
    fields_obj_list = model._meta.fields
    fields = {
        field.name: field.attname for field in fields_obj_list
    }
    return fields


def changes_fields(fields_model, table):
    """Изменяет название полей для корректной записи в БД."""
    for row in table:
        for name_field in list(row):
            if (
                    name_field in fields_model
                    and name_field
                    != fields_model[name_field.replace("_id", "")]
            ):
                row[fields_model[name_field]] = row.pop(name_field)


def load_data(model, name_file):
    """Загрузка данных по имени модели."""
    table = read_csv(name_file)
    changes_fields(get_list_fields_model(model), table)
    model.objects.bulk_create(model(**row) for row in table)


def del_data():
    """Удаляет все таблицы из БД."""
    for model in DATA_CSV:
        model.objects.all().delete()


class Command(BaseCommand):
    help = 'Импортирует таблицы из csv в БД'

    def add_arguments(self, parser):
        parser.add_argument(
            '-a',
            '--all',
            action='store_true',
            help='Импортирует все таблицы из csv в БД'
        )
        parser.add_argument(
            '-c',
            '--clear',
            action='store_true',
            help='Удаляет все данные из БД'
        )

    def handle(self, *args, **options):
        try:
            if options['all']:
                for model, name_file in DATA_CSV.items():
                    load_data(model, name_file)
                self.stdout.write(
                    self.style.SUCCESS('Таблицы загружены в БД.'))
            elif options['clear']:
                del_data()
                self.stdout.write(
                    self.style.SUCCESS('БД успешно очищена.'))
        except django.db.utils.IntegrityError as e:
            self.stdout.write(
                self.style.ERROR(f'Ошибка загрузки: {e}.'))
        except ObjectDoesNotExist:
            self.stdout.write(
                self.style.NOTICE('Нет данных из связанных таблиц'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка загрузки данных: {e}'))
