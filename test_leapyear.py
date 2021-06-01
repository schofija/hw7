import leapyear
import pytest

#Test file for leapyear.py -- Author: Jack Schofield

#pytest functions below

def test_leapyear1():
    assert leapyear.check(1999) == 0
    
def test_leapyear2():
    assert leapyear.check(2004) == 1
    
def test_leapyear3():
    assert leapyear.check(1900) == 0