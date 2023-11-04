import numpy
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2*x + 10


def df(x):
    return 2*x - 2

def newton(x, iterations):
    lst = [x]
    lsty = [f(x)]
    for i in range(iterations):
        x = x - f(x) / df(x)
        lst.append(x)
        lsty.append(f(x))
    return lst, lsty

def printPoint(lst, lsty):
    n = 0
    for i,j in zip(lst, lsty):
        print(f'(x_{n}, y_{n}) = ({i}, {j})')
        n += 1



x = numpy.linspace(-6.5, 10, 1000)
y = f(x)
xx, yy = newton(0, 10)
printPoint(xx, yy)

'''
plt.plot(x, y, xx, yy, 'bs')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Method')
plt.text(2.5, 50, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
plt.show()
'''