
import collections, sys, os
from logic import *

def formula1a():
    Summer = ATOMIC_GROUP('Summer')             
    California = atom_expr('California')       

    Rain = atom('Rain')                 
    formula = Implies(And(Summer, California), Not(Rain))

    return formula