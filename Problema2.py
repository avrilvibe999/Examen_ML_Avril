import collections, sys, os
from logic import *

def formula1b():
    Rain = Atom('Rain')
    Wet = Atom('Wet')
    Sprinklers = Atom('Sprinklers')

    formula = Or(And(Rain, Wet), And(Not(Rain), Sprinklers, Wet))

    return formula

print(formula1b()) 
