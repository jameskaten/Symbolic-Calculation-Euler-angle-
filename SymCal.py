# Robotics
# Euler angle calculation using symbolic-py

from math import *
import sympy as sp
import numpy as np

# define variables
th1 = sp.Symbol('th1')
th2 = sp.Symbol('th2')
th3 = sp.Symbol('th3')
th4 = sp.Symbol('th4')
L1 = sp.Symbol('L1')
L2 = sp.Symbol('L2')
L3 = sp.Symbol('L3')
L4 = sp.Symbol('L4')
L5 = sp.Symbol('L5')

def Rotation_Z(a):
    return sp.Matrix([[sp.cos(a), -sp.sin(a), 0, 0],
                     [sp.sin(a), sp.cos(a), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def Trans_xy(a, b):
    return sp.Matrix([[1,0,0,a],[0,1,0,b],[0,0,1,0],[0,0,0,1]])

Trans_0to1 = sp.simplify(Trans_xy(L1*sp.cos(th1)-L2*sp.sin(th1), L1*sp.sin(th1)+L2*sp.cos(th1))*Rotation_Z(th1))
Trans_1to2 = sp.simplify(Trans_xy(L3*sp.cos(th2), L3*sp.sin(th2))*Rotation_Z(th2))
Trans_2to3 = sp.simplify(Trans_xy(L3*sp.cos(th3), L3*sp.sin(th3))*Rotation_Z(th3))
Trans_3to4 = sp.simplify(Trans_xy(L5*sp.cos(th4)-L4*sp.sin(th4), L5*sp.sin(th4)+L4*sp.cos(th4)))

Trans_0to2 = sp.simplify(Trans_0to1*Trans_1to2)
Trans_0to3 = sp.simplify(Trans_0to1*Trans_1to2*Trans_2to3)
Trans_0to4 = sp.simplify(Trans_0to1*Trans_1to2*Trans_2to3*Trans_3to4)

print('Trans_0to1 = ', Trans_0to1)
print('Trans_0to2 = ', Trans_0to2)
print('Trans_0to3 = ', Trans_0to3)
print('Trans_0to4 = ', Trans_0to4)

