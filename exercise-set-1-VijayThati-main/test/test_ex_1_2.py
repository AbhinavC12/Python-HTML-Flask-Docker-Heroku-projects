"""
Tests for ex_1_1.py
Updated for GitHub: October 2022
"""
import pytest
from src import ex_1_2


def test___last_user_login___exists():
    assert hasattr(ex_1_2, 'last_user_login')
    assert hasattr(ex_1_2.last_user_login, '__call__')


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (
                ['Sly', 'Brockbank', 'sbrockbank0@patch.com', '118', '5/21/2021'],
                tuple,

        ),
    ]
)
def test___last_user_login___returns_tuple(test_input,expected):
    assert isinstance(ex_1_2.last_user_login(test_input), expected)


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (
                ['Sly', 'Brockbank', 'sbrockbank0@patch.com', '5/21/2021'],
                ('sbrockbank0', '5/21/2021')

        ),
        (
                ['Modesta', 'Petegre', 'mpetegre1@kickstarter.com', '10/12/2020'],
                ('mpetegre1', '10/12/2020')
        ),
        (
                ['Karine', 'Woollons', 'kwoollons2@moonfruit.com', '3/26/2021'],
                ('kwoollons2', '3/26/2021')
        ),
        (
                ['Kendricks', 'Vockings', 'kvockings3@state.tx.us', '11/18/2020'],
                ('kvockings3', '11/18/2020')
        ),
    ]
)
def test___last_user_login___returns_user_last_login(test_input,expected):
    assert ex_1_2.last_user_login(test_input) == expected

