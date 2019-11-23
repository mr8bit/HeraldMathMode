from django.test import TestCase

from backend.bot.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(telegram_slug="mr9bit", messenger=0)
        User.objects.create(messenger=1, first_name="Nte", second_name="asd")

    def test_str(self):
        """Animals that can speak are correctly identified"""
        lion = User.objects.get(telegram_slug="mr9bit")
        cat = User.objects.get(name="Nte")
        self.assertEqual(str(lion), 'mr9bit"')
        self.assertEqual(str(cat), 'Nte asd')
