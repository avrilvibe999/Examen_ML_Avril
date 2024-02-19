import collections, sys, os
from logic import *

def formula1d():
    Heads = Atom('Heads')
    Tails = Atom('Tails') 

    formula = Or(Heads, Tails) & Not(And(Heads, Tails))

    return formula

print(formula1d())
