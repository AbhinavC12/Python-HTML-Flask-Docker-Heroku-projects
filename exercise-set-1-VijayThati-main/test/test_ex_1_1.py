"""
Tests for ex_1_1.py
Modified for GitHub: October 2022
"""
from src import ex_1_1


def test___get_username___exists():
    hasattr(ex_1_1, 'get_username')
    hasattr(ex_1_1.get_username, '__call__')


def test___get_username___invalid_begins_with_at___returns_none():
    assert ex_1_1.get_username('@example.com') is None


def test___get_username___invalid_ends_with_at___returns_none():
    assert ex_1_1.get_username('user@') is None


def test___get_username___invalid_no_at___returns_none():
    assert ex_1_1.get_username('user-domain.com') is None


def test___get_username___valid_upper___returns_lowercase_user():
    assert ex_1_1.get_username('USER@EXAMPLE.COM') == 'user'


def test___get_username___valid_lower___returns_user():
    assert ex_1_1.get_username('user@example.com') == 'user'