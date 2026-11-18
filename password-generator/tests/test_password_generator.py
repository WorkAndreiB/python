import pytest
import string
from password_generator import generate_password


def test_generate_password_invalid_length():
    with pytest.raises(ValueError, match="Password length must be at least 1"):
        generate_password(0)
        
def test_generate_password_default_length():
    password = generate_password()
    assert len(password) == 12


def test_generate_password_characters():
    password = generate_password(12)
    allowed_characters = string.ascii_letters + string.digits + string.punctuation
    assert all(c in allowed_characters for c in password)