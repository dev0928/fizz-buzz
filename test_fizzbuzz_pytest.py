import pytest

from fizz_buzz import *


@pytest.mark.parametrize("input,expected_output", 
                         [(9, "Fizz"),
                          (10, "Buzz"),
                          (15, "FizzBuzz"),
                          (23, "23") ])
def test_fizzbuzz_valid_inputs(input,expected_output):
    return_value = fizzbuzz(input)
    assert return_value == expected_output


def test_fizzbuzz_invalid_input():
    with pytest.raises(Exception) as context:
        fizzbuzz("invalid")
        assert str(context.value) == "Invalid Input" 
