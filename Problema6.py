import collections, sys, os
from logic import *

def formula2b():
    def Person(x): return Atom('Person', x)        
    def Child(x, y): return Atom('Child', x, y) 

    
    formula = Exists(Person, And(Person('x'), Forall(Child, Implies(Person('x'), Not(Child('x', 'y'))))))

    return formula

print(formula2b()) 
