import pytest


@pytest.fixture
def prework():
    print("I setup browser instance")

def test_initialcheck(prework):
    print("this is first test")

