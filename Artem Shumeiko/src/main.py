from typing import Union


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers.")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments must be integers.")
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
