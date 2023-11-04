import numpy
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 2*x + 10


def df(x):
    return 2*x - 2

def gradient(x, alpha, iterations):
    lst = [x]
    lsty = [f(x)]
    for i in range(iterations):
        x = x - alpha * df(x)
        lst.append(x)
        lsty.append(f(x))
    return lst, lsty

def newton(x, iterations):
    lst = [x]
    lsty = [f(x)]
    for i in range(iterations):
        x = x - f(x) / df(x)
        lst.append(x)
        lsty.append(f(x))
    return lst, lsty

x = numpy.linspace(-0.5, 2.5, 1000)
y = f(x)
plt.figure(1)
plt.subplot(121)
plt.plot(x, y, color = 'blue')
plt.xlabel('x')
plt.ylabel('y')

xx, yy = gradient(0, 0.1, 10)
plt.plot(xx, yy, 'ro')
plt.text(1, 10, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
plt.title('Gradient Descent Method')

xx2, yy2 = newton(0, 10)

# plot the points (x in -0.5 ~ 2.5) and dont let the points out of the range

plt.subplot(122)
plt.plot(x, y, color = 'blue')
for i,j in zip(xx2, yy2):
    if i >= -0.5 and i <= 2.5:
        plt.plot(i, j, 'bs')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Method')
plt.text(1, 10, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
plt.show()