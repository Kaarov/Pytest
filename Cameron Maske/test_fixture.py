import pytest


@pytest.fixture
def bob():
    return {"name": "Bob"}


def hi(person):
    return "Hi, {name}".format(**person)


def bye(person):
    return "Bye, {name}".format(**person)


def how_are_you(person):
    return "How are you {name}?".format(**person)


def test_hello(bob):
    assert hi(bob) == "Hi, Bob"


def test_bye(bob):
    assert bye(bob) == "Bye, Bob"


def test_how_are_you(bob):
    assert how_are_you(bob) == "How are you Bob?"
