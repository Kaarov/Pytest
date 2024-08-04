import math
import pytest
from source import shapes


class TestCircle:
    def setup_method(self, method):
        print(f"Setting up {method.__name__}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method.__name__}")
        del self.circle

    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = math.pi * self.circle.radius * 2
        assert result == expected
