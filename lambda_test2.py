#  quadratic solver y = ax^2+ bx + c
from math import sqrt

def quadratic_solver(a,b,c):
    root =((-b+ sqrt(b*b-4*a*c))/(2*a),(-b - sqrt(b*b-4*a*c))/(2*a))
    return root

print(quadratic_solver(100,56,3))

# root = lambda a,b,c : ((-b+ sqrt(b*b-4*a*c))/(2*a),(-b - sqrt(b*b-4*a*c))/(2*a))
# print(root(100,56,3))

