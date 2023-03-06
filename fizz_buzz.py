import numbers


def fizzbuzz(input):
    """
    Given a number return Fizz if the number is divisible by 3, 
    return Buzz if the number is divisible by 5, 
    FizzBuzz if the number is divisible by both 3 and 5
    else return the input

    :param input: the number to tested for the Fizz Buzz game
    :return: a string converted based on FizzBuzz game logic

    >>> fizzbuzz(9)
    'Fizz'
    >>> fizzbuzz(10)
    'Buzz'
    >>> fizzbuzz(15)
    'FizzBuzz'
    >>> fizzbuzz(23)
    '23'
    >>> fizzbuzz("invalid")
    Traceback (most recent call last):
    ...
    Exception: Invalid input
    """
    if not isinstance(input, numbers.Number):
        raise Exception("Invalid input")
    
    output = ""
    game_rules = {3: "Fizz", 5: "Buzz"}
    for num in game_rules.keys():
        if input % num == 0:
            output += game_rules[num]
    
    if not output:
        output = str(input)
    
    return output


if __name__ == "__main__":
    import doctest
    doctest.testmod()