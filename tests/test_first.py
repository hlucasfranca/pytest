from util import util

import pytest


@pytest.mark.order(-1)
def test_person(person):    
    
    print(util.transform_payload(person))
    
    assert person["name"] != ""