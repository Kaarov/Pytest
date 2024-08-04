import pytest
import json
from tinydb import TinyDB


@pytest.fixture()
def db():
    db = TinyDB('db.json')
    yield db
    db.truncate()


def test_insert_ont(db):
    db.insert({"name": "Bob"})
    assert len(db.all()) == 1


def test_insert_multiple(db):
    db.insert_multiple(
        [
            {"name": "Alice"},
            {"name": "Carlos"},
        ]
    )
    assert len(db.all()) == 2
