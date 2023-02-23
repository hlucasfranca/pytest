from util import util

def test_person(person):    
    
    print(util.transform_payload(person))
    
    assert person["name"] != ""