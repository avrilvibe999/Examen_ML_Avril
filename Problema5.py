import collections, sys, os
from logic import *

def formula2a_unique_mother():
    def Person(x): return Atom('Person', x)       
    def Mother(x, y): return Atom('Mother', x, y) 

    formula = Forall(Person, Implies(Person('x'), Exists(Mother, And(Mother('y', 'x'), Forall(Mother, Implies(Mother('z', 'x'), Equal('z', 'y')))))))

    return formula
