## Summary

This repo walks through the implementation of different types of unit tests for the classic **FizzBuzz** game where the function returns the word **Fizz** for the multiples of 3, **Buzz** for the multiples of 5, and **FizzBuzz** for the multiples of 3 and 5.

### Virtual Environment ###

1. Install `virtualenv` on Python.
1. Create a virtual environment on the project folder
```
> pip3 install virtualenv
> python3 -m venv venv
> source ./venv/bin/activate
```

### Package Installation ###

With the environment activated you can install packaged using pip:
```
pip install -r requirements.txt
```

To run unit tests, execute the below command from command line:
```
python -m unittest -v
```

To run pytests, execute the below command from command line:
```
python -m pytest -v
```

For doctests:
```
python <module name> -v
```

For getting coverage report in html, run the below commands:
```
> coverage run --source=fizz_buzz.py -m pytest -v test_*.py && coverage report -m
> coverage html
```
