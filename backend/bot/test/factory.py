import factory

from backend.bot import models
import factory.fuzzy


class UserFactory(factory.Factory):
    class Meta:
        model = models.User

    first_name = factory.Faker('first_name')
    second_name = factory.Faker('last_name')
    user_id = factory.fuzzy.FuzzyText(prefix="user_id", length=300)
    messenger = factory.fuzzy.FuzzyChoice(models.User.choices)
    state = factory.fuzzy.FuzzyText(prefix="state", length=300)
    prev_state = factory.fuzzy.FuzzyText(prefix="prev_state", length=300)
    telegram_slug = factory.fuzzy.FuzzyText(prefix="telegram_slug", length=300)
    language = factory.fuzzy.FuzzyChoice(models.User.lang)
    group = factory.fuzzy.FuzzyText(prefix="group", length=300)
