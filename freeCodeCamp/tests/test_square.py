import pytest
from source import shapes


@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_area", [(3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeters(side_length, expected_area):
    assert shapes.Square(side_length).perimeter() == expected_area
