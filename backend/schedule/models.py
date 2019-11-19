from django.db import models
from backend.bot.models import User


class Help(models.Model):
    """
        Млдель оповещений
    """
    choices = (('r', 'Расписание'), ('b', 'Бот'))
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Сообщение")
    date = models.DateTimeField(auto_now=True, verbose_name="Время")
    category = models.CharField(choices=choices, max_length=300)
