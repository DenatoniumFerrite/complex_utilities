import matplotlib.pyplot as plt
from sympy import *
from numpy import linspace

x = Symbol('x')
z = Symbol('z')

def input_functions():
    fx = input("Enter function f(x): ")
    gz = input("Enter function g(z): ")
    return fx, gz

def graph(fx, gz):
    f = lambdify(x, sympify(fx))
    g = lambdify(z, sympify(gz))

    f_x_vals = linspace(-10, 10, 1000)
    f_y_vals = []
    for point in f_x_vals:
        f_y_vals.append(f(point))

    g_x_vals = []
    g_y_vals = []
    for point in range(len(f_x_vals)):
        complex_point = g(f_x_vals[point]+f_y_vals[point]*1j)
        g_x_vals.append(complex_point.real)
        g_y_vals.append(complex_point.imag)

    plt.plot(f_x_vals, f_y_vals, label='f(x)')
    plt.plot(g_x_vals, g_y_vals, label='g(x+f(x)i)')
    plt.legend()
    plt.xlim([-10,10])
    plt.ylim([-10,10])
    plt.show()

print("Input functions. NB: remember to use z as variable in second, remember that the power symbol is ** not ^")
fx, gz = input_functions()
graph(fx, gz)
fx, gz = input_functions()
graph(fx, gz)
