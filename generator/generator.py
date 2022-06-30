from data.data import Person
from faker import Faker


faker_en = Faker('en_US')
Faker.seed()


def generate_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        cur_addr=faker_en.address(),
        permanent_addr=faker_en.address(),
    )
