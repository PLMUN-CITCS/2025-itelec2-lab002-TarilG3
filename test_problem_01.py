# DO NOT MODIFY THE CODE IN THIS FILE

# Test for Problem 1
# Simple Calculator Program

import os.path
import sys
from problem_01 import main
from tud_tests import *

def test_problem_01():

    try:
        exists = os.path.exists('problem_01.py')
        assert exists == True

    except:
        sys.exit('Missing File: problem_01.py')

    set_keyboard_input([5, 5])
    main()
    output = get_display_output()

    try:
        assert output == [
            "Simple Calculator Program",
            "Enter 1st number: ",
            "Enter 2nd number: ",
            "The sum is 10",
            "The difference is 0",
            "The product is 25",
            "The quotient is 1.00"
        ]

    except AssertionError:
        sys.exit('Assertion Error Occurred')
