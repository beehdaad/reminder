import random
import secrets

from django.contrib.auth import get_user_model

from mimesis.locales import Locale
from mimesis import (
    Text,
    Person,
    Address,
    Datetime,
)

User = get_user_model()


class BaseDataGenerator:
    """"""

    def __init__(self, locale='en'):
        self.text = Text(getattr(Locale, locale.upper()))
        self.person = Person(getattr(Locale, locale.upper()))
        self.address = Address(getattr(Locale, locale.upper()))
        self.datetime = Datetime()

    def get_random_secrets(self, nbytes=20):
        return secrets.token_urlsafe(nbytes)

    def get_random_text(self):
        return self.text.text()

    def get_random_words(self, quantity):
        return ' '.join(self.text.words(quantity=quantity))

    def get_random_obj(self, population):
        return random.choice(population)

    def get_random_email(self):
        return self.person.email()

    def get_random_username(self):
        return self.person.username()

    def get_random_password(self, hashed=False):
        return self.person.password(length=20, hashed=hashed)

    def get_random_number(self, start: int = 1, end: int = 100, decimal: bool = False) -> int | float:
        number = random.randint(start, end)
        if decimal == True:
            number = float("{:.1f}".format(random.uniform(start, end)))
        return number

    def get_last_phone_number(self):
        last = 111111111
        if User.objects.exists():
            last = int(User.objects.last().phone_number[2:]) + 1
        return last

    def get_random_phone_number(self, phone_num, index):
        return f"09{phone_num + index}"

    def get_random_country(self):
        return self.address.country(allow_random=True)

    def get_random_city(self):
        return self.address.city()

    def get_random_address(self):
        return self.address.address()

    def get_random_postal_code(self):
        return self.address.postal_code()

    def get_random_first_name(self):
        return self.person.first_name()

    def get_random_last_name(self):
        return self.person.last_name()

    def get_random_datetime(self, start, end):
        return self.datetime.datetime(start, end, timezone='utc')

    def get_random_boolean(self):
        return random.choice((True, False))
