import pytest
from contextlib import nullcontext as does_not_raise

from src.main import Calculator


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, result, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5.0, does_not_raise()),
            (6, "3", 2.0, pytest.raises(TypeError)),
        ]
    )
    def test_divide(self, x: int, y: int, result: float, expectation):
        with expectation:
            assert Calculator().divide(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (6, "3", 9, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, x: int, y: int, result: float, expectation):
        with expectation:
            assert Calculator().add(x, y) == result
