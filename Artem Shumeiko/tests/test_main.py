import pytest

from src.main import Calculator


@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 2, 0.5),
        (5, -1, -5.0),
        (6, 3, 2.0)
    ]
)
def test_divide(x: int, y: int, result: float):
    assert Calculator().divide(x, y) == result


@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 2, 3),
        (5, -1, 4),
        (6, 3, 9)
    ]
)
def test_add(x: int, y: int, result: float):
    assert Calculator().add(x, y) == result
