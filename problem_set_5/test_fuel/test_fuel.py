import pytest
from fuel import convert,gauge

def main():
    test_empty()
    test_full()
    test_mid()
    test_char()

def test_empty():

    assert convert("1/100")==1 and gauge(1)=="E"
    assert convert("0/33")==0 and gauge(0)=="E"
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_full():
    assert convert("4/4")==100 and gauge(100)=="F"
    assert convert("99/100")==99 and gauge(99)=="F"

def test_mid():
    assert convert("1/4")==25 and gauge(25)=="25%"
    assert convert("1/2")==50 and gauge(50)=="50%"
    assert convert("1/33")==3 and gauge(3)=="3%"

def test_char():
    with pytest.raises(ValueError):
        convert("cat/dog")


if __name__=="__main__":
    main()
