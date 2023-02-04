"""
Tests for ex_1_4.py
Updated for GitHub: October 2022
"""
import pytest
from src import ex_1_4


def test___get_username___exists():
    assert hasattr(ex_1_4, 'get_username')
    assert hasattr(ex_1_4.get_username, '__call__')


def test___get_username___begins_with_at___raises_value_error():
    with pytest.raises(ValueError):
        ex_1_4.get_username('@example.com')


def test__get_username___ends_with_at___raises_value_error():
    with pytest.raises(ValueError):
        ex_1_4.get_username('user@')


def test_get_username___no_at_in_email___raises_value_error():
    with pytest.raises(ValueError):
        ex_1_4.get_username('user-domain')


def test_get_username___integer_input___raises_type_error():
    with pytest.raises(TypeError):
        ex_1_4.get_username(10)


def test_get_username___list_input___raises_type_error():
    with pytest.raises(TypeError):
        ex_1_4.get_username(['user', 'domain'])


def test___get_username___dict_input___raises_type_error():
    with pytest.raises(TypeError):
        ex_1_4.get_username({'user': 'domain'})


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('user@domain.com', 'user'),
        ('USER@DOMAIN.com', 'user')
    ]
)
def test___get_username___valid_email___returns_lowercase_username(test_input, expected):
    assert ex_1_4.get_username(test_input) == expected
