import logging

import telegram
from django.conf import settings
from telegram import ParseMode

from backend.bot.messangers.core import BaseTrigger
from backend.bot.models import User

logger = logging.getLogger(__name__)


class TelegramTrigger(BaseTrigger):
    """
        Телеграм триггер для State Machine
    """

    def __init__(self, telegram_slug, **kwds):
        self.telegram_slug = telegram_slug
        super().__init__(**kwds)

    def send_keyboard(self, message, buttons, whom=None):
        """
            Отправка клавиатуры
        :param message: Текст для отправки
        :param buttons: Кнопки для отправки в формате массива
        :param whom: id чата для отправки
        :return: None
        """
        kb = []
        for button in buttons:
            kb.append([telegram.KeyboardButton(button)])
        kb_markup = telegram.ReplyKeyboardMarkup(kb)
        self.client.sendMessage(parse_mode=ParseMode.HTML,
                                chat_id=self.user_id,
                                text=message,
                                reply_markup=kb_markup)

    def send_message(self, message, whom=None):
        """
            Отправка сообщения
        :param message: текст сообщения
        :param whom: id чата для отпавки (необязательное)
        :return:
        """
        destination = whom or self.user_id
        self.client.sendMessage(destination, text=message, parse_mode=ParseMode.HTML)

    def send_photo(self, image_path):
        """
            Отправка фотографии
        :param image_path: Путь на самом сервере
        :return:
        """
        destination = self.user_id
        photo_path = "{}/{}".format(settings.MEDIA_ROOT, image_path)
        self.client.send_photo(chat_id=destination, photo=open(photo_path, 'rb'))

    def send_document(self, document_path):
        """
            Отправка документа
        :param document_path: Путь на самом сервере
        :return:
        """
        destination = self.user_id
        document_path = "{}/{}".format(settings.MEDIA_ROOT, document_path)
        self.client.send_document(chat_id=destination, document=open(document_path, 'rb'))

    def get_user(self, whom=None):
        """
            Получение пользователя из базы данных
        :param whom: id пользователя
        :return: User объект пользователя
        """
        try:
            usr = User.objects.get(user_id=self.user_id)
            return usr
        except Exception as e:
            logger.warning("Error on get user: {}".format(e))
            return False

    def create_user(self):
        """
            Создание пользователя
        :return: None
        """
        try:
            new_user = User.objects.create(user_id=self.user_id, telegram_slug=self.telegram_slug,
                                           messenger=self.messenger)
            new_user.save()
            return True
        except Exception as e:
            return False
