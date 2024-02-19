import collections, sys, os
from logic import *

def parentChild():
    def Parent(x, y): return Atom('Parent', x, y) 
    def Child(x, y): return Atom('Child', x, y)
    formula = Forall(Child, Implies(Child('x'), Exists(Parent, And(Parent('y', 'x'), Forall(Child, Implies(Child('z'), Equal('z', 'x'))))))) & Forall(Parent, Implies(Parent('y'), Exists(Child, And(Child('z', 'y'), Forall(Parent, Implies(Parent('w', 'y'), Equal('w', 'z')))))))

    return formula
print(parentChild())
