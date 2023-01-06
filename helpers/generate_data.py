from dataclasses import dataclass
from faker import Faker
faker_en = Faker('En')

@dataclass
class Randomdata:
    first_name: str = None
    email: str = None
    last_name: str = None
    user_name: str = None
    password: str = None
    
def generated_data():
    yield Randomdata(
        email = faker_en.email(),
        first_name = faker_en.first_name(),
        last_name = faker_en.last_name(),
        user_name = faker_en.user_name(),
        password = faker_en.password(10)
    )