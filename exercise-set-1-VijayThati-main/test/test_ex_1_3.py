"""
Tests for ex_1_3.py
Updated for GitHub: October 2022
"""
import pytest
from src import ex_1_3

accounts_1 = [
    ['Sly', 'Brockbank', 'sbrockbank0@patch.com', '5/21/2021'],
    ['Modesta', 'Petegre', 'mpetegre1@kickstarter.com', '10/12/2020'],
]

accounts_2 = [
    ['Wilt', 'Vasyunichev', 'wvasyunichev8@senate.gov', '10/16/2021'],
    ['Conchita', 'Poupard', 'cpoupard9@icq.com', '4/5/2021']
]

accounts_1_dict = {
        'sbrockbank0': '5/21/2021',
        'mpetegre1': '10/12/2020',
}


accounts_2_dict = {

       'wvasyunichev8': '10/16/2021',
       'cpoupard9': '4/5/2021',
}


def test___last_logins___exists():
    assert hasattr(ex_1_3, 'last_logins')
    assert hasattr(ex_1_3.last_logins, '__call__')


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (accounts_1, accounts_1_dict),
    ]
)
def test___last_logins___returns_dict(test_input, expected):
    actual = ex_1_3.last_logins(test_input)
    assert isinstance(actual, dict)


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (accounts_1, accounts_1_dict),
        (accounts_2, accounts_2_dict),
    ]
)
def test__last_logins___returns_correct_values(test_input, expected):
    assert ex_1_3.last_logins(test_input) == expected
