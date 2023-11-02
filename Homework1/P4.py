import numpy
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def Graph(x, y, title):
    plt.plot(x, y)
    plt.xlabel('x', loc = 'right')
    plt.ylabel('y', loc = 'top', rotation = 0)
    plt.title(title)
    x_center = (x[0] + x[-1]) / 2
    y_center = max(y) - (max(y) - min(y)) / 2
    plt.text(x_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
    plt.show()

def a(x):
    return numpy.exp((x**2) * -0.5)

def b(x):
    return numpy.tan(0.5 * (x ** 2) + x + 1)

def d(x):
    return -x - 1 + numpy.tan(x)

x = numpy.linspace(-3, 3, 100)
y = a(x)

Graph(x, y, r'$ y = e^{\frac{-x^2}{2}} $')

x = numpy.linspace(0, 5, 100)
y = b(x)

Graph(x, y, r'$ y = tan(\frac{x^2}{2} + x + C ), C=1 $')

x = numpy.linspace(0, 5, 100)
y = d(x)

Graph(x, y, r'$ y = -x - 1 + tan(x) $')