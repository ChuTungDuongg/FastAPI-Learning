def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1
    
def test_is_instance():
    assert isinstance(3, int)
    assert not isinstance("10", int)
    
def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False
    
def test_type():
    assert type(3) == int
    assert (type("hello") is not int)
    
def test_greater_and_less_than():
    assert 7 > 3
    assert 4 < 10
    assert not (5 < 3)
    assert not (2 > 4)
    
