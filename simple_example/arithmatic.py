"""Arithmatic"""

from typing import Union


def add(lhs: Union[int, float], rhs: Union[int, float]) -> Union[int, float]:
    """Add two numbers.

    Args:
        lhs (Union[int, float]): The left hand side
        rhs (Union[int, float]): The right hand side

    Returns:
        Union[int, float]: The addition of two numbers.
    """
    return lhs + rhs


def subtract(lhs: Union[int, float], rhs: Union[int, float]) -> Union[int, float]:
    """Subtract two numbers.

    Args:
        lhs (Union[int, float]): The left hand side
        rhs (Union[int, float]): The right hand side

    Returns:
        Union[int, float]: The subtraction of two numbers.
    """
    return lhs - rhs


def multiply(lhs: Union[int, float], rhs: Union[int, float]) -> Union[int, float]:
    """Multiply two numbers.

    Args:
        lhs (Union[int, float]): The left hand side
        rhs (Union[int, float]): The right hand side

    Returns:
        Union[int, float]: The multiplication of two numbers.
    """
    return lhs * rhs


def divide(lhs: Union[int, float], rhs: Union[int, float]) -> Union[int, float]:
    """Divide two numbers.

    Args:
        lhs (Union[int, float]): The left hand side
        rhs (Union[int, float]): The right hand side

    Returns:
        Union[int, float]: The division of two numbers.
    """
    return lhs / rhs
