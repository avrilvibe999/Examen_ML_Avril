import collections, sys, os
from logic import *

def formula1c():
    Day = Atom('Day')
    Night = Atom('Night')

    formula = Or(Day, Night) & Not(And(Day, Night))
    return formula

print(formula1c()) 
