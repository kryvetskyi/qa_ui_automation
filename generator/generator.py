import random

from faker import Faker

from data.data import Person

faker_en = Faker("en_US")
Faker.seed()


def generate_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        age=random.randint(18, 100),
        department=faker_en.job()[:25],     # only 25 symbols are accepted  for this field
        salary=random.randint(2000, 20000),
        email=faker_en.email(),
        cur_addr=faker_en.address(),
        permanent_addr=faker_en.address(),
        mobile=faker_en.msisdn()[:10],
    )
