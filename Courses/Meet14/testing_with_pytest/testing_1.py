"""
PYTEST
"""

# functia noastra
import pytest


def rectangle_area(l, L):
    return l * L


def test_rectangle_area():
    assert rectangle_area(3, 5) == 15


@pytest.mark.skip
def test_should_be_skipped():
    assert rectangle_area(-2, 0) == 0


@pytest.mark.xfail
def test_should_be_skipped_xfail():
    assert rectangle_area(-3, 1) == -3


@pytest.mark.slow
def test_should_be_skipped_slow():
    assert rectangle_area(-3, 0) == 0

#ToDo  - simularea unui calc, validat prin pytest
