from backend.bot.messangers.core import BaseState as State
from .utils import get_today_schedule, get_next_day_schedule
from datetime import datetime


class BootStrapState(State):
    def on_trigger(self, trigger):
        try:
            trigger.create_user()
        except:
            trigger.get_user()
        return EnterSecretCode()


class EnterSecretCode(State):
    """
        Вход на главный экран и ввод секретного пароля
    """

    def __init__(self):
        self.buttons = ['', ]
        self.text = 'Приветствую, на весенней школе математического моделирования в ☀️Алуште.\n\nДля дальнейшего пользования, напишите свою фамилию с большой буквы\nПример: Иванов'

    def on_enter(self, trigger):
        trigger.send_message(self.text)

    def on_trigger(self, trigger):
        user = trigger.get_user()
        user.second_name = trigger.text
        user.save()
        return MainMenu()


class MainMenu(State):
    """
        Главное меню
    """

    def __init__(self):
        self.buttons = ['📅 Расписание', '🗺️ Карта', '🌐 VPN', '📶 WiFi']
        self.text = 'Главное меню'

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return Schedule()
        if trigger.text == self.buttons[1]:
            return Map()
        if trigger.text == self.buttons[2]:
            return VPN()
        if trigger.text == self.buttons[3]:
            return WiFi()
        trigger.send_keyboard("Не разобрал вас, повторите", self.buttons)


class Map(State):
    """
        Карта конференции
    """

    def __init__(self):
        self.buttons = ['🔙 Назад', ]
        self.text = "Карта мероприятия"

    def on_enter(self, trigger):
        trigger.send_photo('map.jpg')
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return MainMenu()


class VPN(State):
    """
        Настройки VPN
    """

    def __init__(self):
        self.buttons = ['🔙 Назад', ]
        self.text = """<b>Спонсор VPN\nСтуденчиский клуб Lambda.</b>\n
<b>Lambda</b> - студенческий практикум программистов при Московском Авиационном Институте\n
<b>Lambda</b> — это:
    🔸лекции и обмен опытом;
    🔸стартапы и гранты;
    🔸хакатоны и олимпиады;
    🔸площадка для выступлений экспертов из IT компаний.
Если Вы:
    💻 хотите создавать сайты, приложения или игры в команде студентов;
    📚 нагружены теорией программирования и хотите применить свои навыки;
    😎 программист и хотите поделиться опытом со студентами;
    🚩 только в начале пути и хотите научиться практическому программированию и разработке
Обязательно приходите на наши собрания. Скучно не будет точно!
https://lambda-it.ru/"""
        self.helper_text = """ Для работы с VPN потребуется OpenVPN\n
- для <a href="https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=ru&gl=US">Android</a>
- для <a href="https://apps.apple.com/ru/app/openvpn-connect/id590379981">iOS</a>
- для <a href="https://openvpn.net/community-downloads/">Windows</a>
- для <a href="https://openvpn.net/client-connect-vpn-for-mac-os/">MacOS</a>
- для Linux разберетесь сами 🤷"""
        self.text_wait = "Происходит генерация VPN ключей, как завершиться мы вас оповестим"

    def on_enter(self, trigger):
        # trigger.send_document('admin.ovpn')
        # trigger.send_message(self.helper_text)
        trigger.send_keyboard(self.text_wait, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return MainMenu()


class Schedule(State):
    """
        Расписание МАИ
    """

    def __init__(self):
        self.buttons = ['Сегодня', 'Завтра', '🔙 Назад']
        self.text = 'Расписание'

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return ScheduleToday()
        if trigger.text == self.buttons[1]:
            return ScheduleNextDay()
        if trigger.text == self.buttons[2]:
            return MainMenu()
        trigger.send_keyboard("клик", self.buttons)


class ScheduleToday(State):
    """
        Расписание сегодня в текущий день по дате
    """

    def __init__(self):
        self.buttons = ['🔙 Назад']

    def on_enter(self, trigger):
        res = ""
        today = get_today_schedule()
        for item in today:
            res += item['title'] + '\n'
            res += "📍 " + item['location'] + '\n'
            time_start = datetime.fromisoformat(item['time_start'])
            time_end = datetime.fromisoformat(item['time_end'])
            new_format = "%H:%M"
            res += "🕑 " + str(time_start.strftime(new_format)) + " - " + str(time_end.strftime(new_format)) + '\n'
            res += '\n'
        trigger.send_keyboard(res, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return Schedule()


class ScheduleNextDay(State):
    """
        Расписание сегодня в текущий день по дате
    """

    def __init__(self):
        self.buttons = ['🔙 Назад']

    def on_enter(self, trigger):
        res = ""
        today = get_next_day_schedule()
        for item in today:
            res += item['title'] + '\n'
            res += "📍 " + item['location'] + '\n'
            time_start = datetime.fromisoformat(item['time_start'])
            time_end = datetime.fromisoformat(item['time_end'])
            new_format = "%H:%M"
            res += "🕑 " + str(time_start.strftime(new_format)) + " - " + str(time_end.strftime(new_format)) + '\n'
            if item["speaker"]:
                res += "👤 " + item["speaker"] + "\n"
            res += '\n'
        trigger.send_keyboard(res, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return Schedule()


class WiFi(State):
    """
        Данные по вайфай
    """

    def __init__(self):
        self.buttons = ['🔙 Назад', ]
        self.text = 'На территории Алушты стоят 2 точки 📶WiFi.\n\n1. 📶MAI - не имеет пароля, необхоидмо произвести авторизацию путем звонка на указанный телефон\n\n2. 📶IT-CENTER - пароль mathmode'

    def on_enter(self, trigger):
        trigger.send_keyboard(self.text, self.buttons)

    def on_trigger(self, trigger):
        if trigger.text == self.buttons[0]:
            return MainMenu()
        else:
            trigger.send_keyboard("Не разобрал вас, повторите", self.buttons)
