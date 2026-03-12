from utils.calculator import Calculator


def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5, "Addition should return the sum of two numbers"


def test_discard():
    calc = Calculator()
    assert (
        calc.discard(5, 2) == 3
    ), "Discard should return the difference of two numbers"


def test_multiply():
    calc = Calculator()
    assert (
        calc.multiply(4, 3) == 12
    ), "Multiplication should return the product of two numbers"


def test_divide():
    calc = Calculator()
    assert (
        calc.divide(10, 2) == 5
    ), "Division should return the quotient of two numbers"


def test_divide_by_zero():
    calc = Calculator()
    try:
        calc.divide(10, 0)
        assert False, "Division by zero should raise ValueError"
    except ValueError as e:
        assert (
            str(e) == "Cannot divide by zero"
        ), f"Expected error message for division by zero, got: {str(e)}"
