import logging

from telegram.ext import MessageHandler, Filters, CommandHandler

from backend.bot.models import User
from backend.bot.handlers.telegram.trigger import TelegramTrigger
from backend.bot.apps import DjangoTelegramBot
from backend.bot.handlers.core.state_machine import StateMachine
from backend.bot.states import BootStrapState

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def start(bot, update):
    machine = StateMachine(initial_state=BootStrapState())
    try:
        usr = User.objects.get(user_id=update.message.chat_id).state
    except Exception as e:
        usr = None
    trigger = TelegramTrigger(
        client=bot,
        user_id=update.message.chat_id,
        messenger=0,
        text=update.message.text,
        user_state=usr
    )
    machine.fire(trigger)


def main():
    logger.info("Loading handlers for telegram bot")
    dp = DjangoTelegramBot.dispatcher
    dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(CommandHandler('start', start))  # Telegram send start message
    dp.add_error_handler(error)
