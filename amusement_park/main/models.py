from django.db import models
from ast import increment_lineno

class Attractions(models.Model):
    id = models.IntegerField("№", primary_key=True)

    time = models.CharField("Час катання", max_length=20)

    name = models.CharField("Назва атракціону", max_length=20)

    min_age = models.IntegerField("Мінімальний вік")

    zone = models.IntegerField("Зона розташування")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'my_administrator/attractions/{self.id}'


class Client(models.Model):
    id = models.IntegerField("№", primary_key=True)

    name = models.CharField("Ім'я", max_length=20)

    surname = models.CharField("Прізвище", max_length=20)

    age = models.IntegerField("Вік")

    registration_date = models.DateField("Дата реєстрації")

    def __str__(self):
        return " ".join([self.name, self.surname])


class Worker(models.Model):
    id = models.IntegerField("№", primary_key=True)

    name = models.CharField("Ім'я", max_length=20)

    surname = models.CharField("Прізвище", max_length=20)

    age = models.IntegerField("Вік")

    address = models.CharField("Адреса", max_length=100)

    def __str__(self):
        return " ".join([self.name, self.surname])
