from django.test import TestCase

from backend.bot.test.factory import UserFactory, NotificationFactory


class UserTestCase(TestCase):
    def test_str(self):
        telegram_user = UserFactory(telegram_slug="mr9bit", messenger=0)
        other_messenger_user = UserFactory(telegram_slug=None, first_name="John", second_name="Good")

        self.assertEqual(telegram_user.__str__(), 'mr9bit')
        self.assertEqual(other_messenger_user.__str__(), 'John Good')


class NotificationTestCase(TestCase):
    def test_str(self):
        notification = NotificationFactory()
        self.assertEqual(notification.__str__(), notification.name)
