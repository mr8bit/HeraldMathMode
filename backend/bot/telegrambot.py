import logging

from telegram.ext import MessageHandler, Filters, CommandHandler

from backend.bot.messangers.trigger import TelegramTrigger
from backend.bot.apps import DjangoTelegramBot
from backend.bot.messangers.core.state_machine import StateMachine
from backend.schedule.states import BootStrapState
from backend.bot.models import User, Request, Error

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def start(bot, update):
    machine = StateMachine(initial_state=BootStrapState())
    ########### Сохраянем статистику в БД ###########
    try:
        usr = User.objects.get(user_id=update.message.chat_id)
        Request.create_request(user=usr, state=usr.state, text=update.message.text)  # сохраняем запрос
        state = usr.state
    except Exception as e:
        state = None
    ########### Сохраянем статистику в БД ###########

    trigger = TelegramTrigger(
        client=bot,
        user_id=update.message.chat_id,
        messenger=0,
        text=update.message.text,
        user_state=state,
        telegram_slug=update.message.chat.username
    )
    machine.fire(trigger)


def main():
    logger.info("Loading handlers for telegram bot")
    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(CommandHandler('start', start))  # Telegram send start message
    dp.add_error_handler(error)
