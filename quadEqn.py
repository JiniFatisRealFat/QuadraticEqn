# A program to calculate Quadratic Equation

import cmath

# Value inputting area
a = int(input("Value for a : "))
b = int(input("Value for b : "))
c = int(input("Value for c : "))

# now the calculation Area

# Calculating the discriminant first
d = b*b-4*a*c

sol1 = (-b-cmath.sqrt(d))/(2*a)

sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solutions are {0} and {1}".format(sol1,sol2))

