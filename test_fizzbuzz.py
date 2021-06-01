import fizzbuzz
import pytest

#Test file for fizzbuzz.py -- Author: Jack Schofield

#pytest functions below

def test_fizzbuzz1():
    assert fizzbuzz.printNum(1) == 1
    
def test_fizzbuzz2():
    assert fizzbuzz.printNum(9) == "fizz"
    
def test_fizzbuzz3():
    assert fizzbuzz.printNum(10) == "buzz"
    
def test_fizzbuzz4():
    assert fizzbuzz.printNum(15) == "fizzbuzz"