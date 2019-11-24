from backend.bot.messangers.core import BaseState as State
from backend.schedule.states import main, init


class Settings(State):
    def __init__(self):
        self.text = "⚙️Настройки"
        self.buttons = ['Сменить номер группы', '🔙Назад']

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return init.EnterGroup()
        elif trigger.text == self.buttons[1]:
            return main.MainMenu()
        else:
            trigger.send_message("Не понял вас ¯\_(ツ)_/¯")
            return Settings()
