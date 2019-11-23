from django.db import models
from backend.bot.models import User


class Help(models.Model):
    """
        Жалобы пользователей
    """
    choices = (('schedule', 'Расписание'), ('bot', 'Бот'), ('other', 'Другое'))
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.DO_NOTHING)
    message = models.TextField(verbose_name="Сообщение")
    date = models.DateTimeField(auto_now=True, verbose_name="Время создания")
    category = models.CharField(choices=choices, max_length=300)
    has_answer = models.BooleanField(default=False, verbose_name="Был ответ")


class AnswerOnHelpSerializer(models.Model):
    """
        Ответ на вопрос
    """
    text = models.TextField(verbose_name="Ответ", default="")
    help = models.ForeignKey(Help, verbose_name="Претензия пользователя", on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True, verbose_name="Время создания")
