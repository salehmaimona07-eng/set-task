from main import check_password_length

def test_valid_password():
    assert check_password_length("strongpass123") == True

def test_short_password():
    assert check_password_length("12345") == False