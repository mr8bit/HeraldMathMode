from django.conf import settings
from django.urls import path

from backend.bot import views

webhook_base = settings.TELEGRAM_BOT.get('WEBHOOK_PREFIX', '/')

if webhook_base.startswith("/"):
    webhook_base = webhook_base[1:]
if not webhook_base.endswith("/"):
    webhook_base += "/"

urlpatterns = [

    path('{}<str:bot_token>/'.format(webhook_base), views.webhook, name='webhook_telegram'),

    path('{0}'.format(settings.VK_BOT.get("WEBHOOK_PREFIX")), views.vk_bot, name='webhook_vk'),

]
