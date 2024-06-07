import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.db import models


class Person(models.Model):
    profileId = models.CharField(max_length=255, default=str(uuid.uuid4()))
    birthdate = models.DateField()
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def set_password(self, raw_pwd):
        self.password = make_password(raw_pwd)
        return None

    def check_password(self, raw_pwd):
        return check_password(raw_pwd, self.password)


class Todo(models.Model):
    identifier = models.CharField(max_length=255, verbose_name='Identifier')
    description = models.CharField(max_length=255, verbose_name='Todo description')
    deadline = models.CharField(max_length=255, verbose_name='Deadline')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
