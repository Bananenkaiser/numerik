import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import brentq, bisect, newton, fsolve

def f(x):
    return np.exp(-x) - np.sin(x)

# Intervallgrenzen, zwischen denen die Nullstelle gesucht wird
a = 0.1
b = 1.5
xtol = 1.e-8

# Verwende die Brent- und Bisektionsmethoden, um die Nullstelle zu finden
nullstelle1 = bisect(f, a, b, xtol=xtol)
nullstelle2 = brentq(f, a, b, xtol=xtol)

# Verwende die Newton-Methode, um die Nullstelle zu finden

# Hier wird nur ein Startwert benötigt
startwert = 1.0  # ein vernünftiger Startwert innerhalb des Intervalls [a, b]
nullstelle3 = newton(f, startwert, tol=xtol)

print(f"Die Nullstelle mit bisect liegt bei: {nullstelle1}")
print(f"Die Nullstelle mit brent liegt bei: {nullstelle2}")
print(f"Die Nullstelle mit newton liegt bei: {nullstelle3}")

# 2 dimensionale Lösungen

def equations(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 4  # Kreisgleichung x^2 + y^2 = 4
    eq2 = x**2 - y - 1     # Parabelgleichung x^2 - y = 1
    return [eq1, eq2]

# Startwerte für x und y
initial_guess = [1, 1]
print(type(initial_guess))
# Löse das Gleichungssystem
solution = fsolve(equations, initial_guess)

print(f"Die Lösung des Systems ist: {solution}")
