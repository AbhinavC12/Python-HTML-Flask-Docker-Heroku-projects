"""
Tests for ex_1_0.py
"""
import pytest
from src import ex_1_0
BASE_RANGE = (0, 10)

def test____in_range___exists():
    assert hasattr(ex_1_0, 'in_range')
    assert hasattr(ex_1_0.in_range, '__call__')


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [(-1, *BASE_RANGE), False],
        [(-2, *BASE_RANGE), False],
        [(-3, *BASE_RANGE), False]
    ]
)
def test___in_range___value_less_than_vmin(test_input, expected):
    assert ex_1_0.in_range(*test_input) == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [
        [(11, *BASE_RANGE), False],
        [(12, *BASE_RANGE), False],
        [(13, *BASE_RANGE), False]
    ]
)
def test___in_range___value_greater_than_vmax(test_input, expected):
    assert ex_1_0.in_range(*test_input) == expected

@pytest.mark.parametrize(
    "test_input,expected",
    [
        [(11, 11, 20), True],
        [(12, 12, 20), True],
        [(13, 13, 20), True]
    ]
)
def test__in_range___value_equals_vmin(test_input, expected):
    assert ex_1_0.in_range(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [(20, 11, 20), True],
        [(30, 12, 30), True],
        [(40, 13, 40), True]
    ]
)
def test___in_range___value_equals_vmax(test_input, expected):
    assert ex_1_0.in_range(*test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [(15, 11, 20), True],
        [(15, 12, 30), True],
        [(15, 13, 40), True]
    ]
)
def test___in_range___value_greater_than_vmin_less_than_vmas(
        test_input,
        expected
):
    assert ex_1_0.in_range(*test_input) == expected


###  is_even tests
def test___is_even___exists():
    assert hasattr(ex_1_0, 'is_even')
    assert hasattr(ex_1_0.is_even, '__call__')


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [3, False],
        [5, False],
        [7, False],
        [10001, False],
    ]
)
def test___is_even___odd_input(test_input, expected):
    assert ex_1_0.is_even(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        [4, True],
        [6, True],
        [8, True],
        [1000, True],
    ]
)
def test___is_even___even_input(test_input, expected):
    assert ex_1_0.is_even(test_input) == expected
