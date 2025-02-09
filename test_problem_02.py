# DO NOT MODIFY THE CODE IN THIS FILE

# Test for Problem 2
# Square the Number Program

import os.path
import sys
from problem_02 import main
from tud_tests import *

def test_problem_02():

    try:
        exists = os.path.exists('problem_02.py')
        assert exists == True

    except:
        sys.exit('Missing File: problem_02.py')

    set_keyboard_input([5])
    main()
    output = get_display_output()

    try:
        assert output == [
            "Square the Number Program",
            "Enter a number: ",
            "The square of 5 is 25.00"
        ]

    except AssertionError:
        sys.exit('Assertion Error Occurred')
