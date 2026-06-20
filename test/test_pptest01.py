import pytest

@pytest.fixture(scope = "function")
def prework():
    print("I setup browser instance")

def test_one(prework):
    print("this is first test")

def test_two(prework):
    print("this is second test")

