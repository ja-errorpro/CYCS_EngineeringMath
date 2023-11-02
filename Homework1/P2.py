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

xx, yy = gradient(0, 0.1, 9)

plt.figure(1)
#plt.subplot(121)
plt.plot(x, y, xx, yy, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gradient Descent Method')
plt.text(1, 10, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
plt.show()


x = numpy.linspace(-5, 10, 1000)
y = f(x)
xx, yy = newton(0, 9)

#plt.subplot(122)


plt.plot(x, y, xx, yy, 'ro')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Method')

plt.text(2.5, 50, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)

plt.show()