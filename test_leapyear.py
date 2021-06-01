import leapyear
import pytest

#Test file for leapyear.py -- Author: Jack Schofield

#pytest functions below

def test_leapyear1():
    assert leapyear.check(1999) == 0