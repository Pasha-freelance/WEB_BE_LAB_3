from django.db import models


class Todo(models.Model):
    identifier = models.CharField(max_length=255, verbose_name='Identifier')
    description = models.CharField(max_length=255, verbose_name='Todo description')
    deadline = models.CharField(max_length=255, verbose_name='Deadline')

    def __str__(self):
        return f"{self.description}"

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
