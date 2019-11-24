from backend.bot.messangers.core.state import BaseState as State
from backend.schedule.models import Issue as HelpModel
from backend.schedule.states import main


class Help(State):
    def __init__(self):
        self.text = 'Выбери категорию проблемы'
        self.buttons = ["Проблема с ботом", "Проблема с расписанием", "Другое", "Назад"]

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return ProblemBot()
        if trigger.text == self.buttons[1]:
            return ProblemSchedule()
        if trigger.text == self.buttons[2]:
            return ProblemOther()
        if trigger.text == self.buttons[3]:
            return main.MainMenu()


class ProblemOther(State):
    def __init__(self):
        self.text = "Опишите свою проблему"
        self.buttons = ["Назад"]

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return Help()
        help = HelpModel.objects.create(user=trigger.get_user(), message=trigger.text, category='other')
        help.save()
        trigger.send_message("Спасибо вам обращение, мы скоро вам ответим")
        return main.MainMenu()


class ProblemSchedule(State):
    def __init__(self):
        self.text = "Опишите свою проблему"
        self.buttons = ["Назад"]

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return Help()
        help = HelpModel.objects.create(user=trigger.get_user(), message=trigger.text, category='schedule')
        help.save()
        trigger.send_message("Спасибо вам обращение, мы скоро вам ответим")
        return main.MainMenu()


class ProblemBot(State):
    def __init__(self):
        self.text = "Опишите свою проблему"
        self.buttons = ["Назад"]

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return Help()
        help = HelpModel.objects.create(user=trigger.get_user(), message=trigger.text, category='bot')
        help.save()
        trigger.send_message("Спасибо вам обращение, мы скоро вам ответим")
        return main.MainMenu()
