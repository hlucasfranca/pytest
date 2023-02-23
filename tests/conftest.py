import pytest

from mimesis import Person

from mimesis import Food
from mimesis import Datetime
from mimesis import Address
from mimesis.locales import Locale

@pytest.fixture(scope="session")
def person():
    person_br = Person(Locale.PT_BR)    
    date_time_br = Datetime(Locale.PT_BR)
    address_br = Address(Locale.PT_BR)
    
    data = {
        "name": person_br.full_name(),
        "email": person_br.email(),
        "phone": person_br.telephone(mask='119########'),
        "birth_date": date_time_br.formatted_date(start= date_time_br._CURRENT_YEAR - person_br.age(minimum=18), end=2000, fmt='%Y-%m-%d'),
        "city": address_br.city(),
        "cep": address_br.postal_code(),
        "address": address_br.street_name()    
    }
    
    yield data