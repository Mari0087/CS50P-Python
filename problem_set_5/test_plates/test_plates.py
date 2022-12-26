from plates import is_valid

def main():
    test_begining()
    test_length()
    test_mid_number()
    test_zero()
    test_characters()

def test_begining():

    assert is_valid("50")==False
    assert is_valid("5C")==False
    assert is_valid("CS")==True

def test_length():

    assert is_valid("CS")==True
    assert is_valid("NRVOUS")==True
    assert is_valid("NRVOHUS")==False
    assert is_valid("ECTO88")==True
    assert is_valid("H")==False
    assert is_valid("OUTATIME")==False

def test_mid_number():
    assert is_valid("CS50")==True
    assert is_valid("CS50P2")==False
    assert is_valid("CS50P")==False

def test_zero():
    assert is_valid("CS05")==False
    assert is_valid("CST056")==False

def test_characters():
    assert is_valid("PI3.14")==False
    assert is_valid("PI3!14")==False
    assert is_valid("PI@14")==False


if __name__=="__main__":
    main()