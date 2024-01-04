import numpy
import matplotlib.pyplot as plt

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
count = 0
def Graph(x, y, title):
    global count
    plt.subplot(2, 3, count + 1)
    plt.plot(x, y)
    plt.xlabel('x', loc = 'right')
    plt.ylabel('y', loc = 'top', rotation = 0)
    plt.title(title)
    x_center = (x[0] + x[-1]) / 2
    y_center = max(y) - (max(y) - min(y)) / 2
    plt.text(x_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
    #plt.show()
    count += 1

def pA(x):
    return numpy.exp(-x)*(2*numpy.cos(3*x) + (0.333)*numpy.sin(3*x))

def pB(x):
    return numpy.exp(-x)*(numpy.cos(3*x) + (0.333)*numpy.sin(3*x))

def pC(x):
    return numpy.exp(-x)+numpy.exp(x)*numpy.cos(x) + numpy.exp(x)*numpy.sin(x)

def pD(x):
    return numpy.exp(4*x)+numpy.exp(-4*x)-(1/8)*numpy.exp(-4*x)*x

def pE(x):
    return numpy.cos(2*x)+0.25*x*numpy.sin(2*x)

def pF(x):
    return x + x**2 + x*numpy.exp(x)

x = numpy.linspace(0, 1, 10000)
y = pA(x)
Graph(x, y, r'$ y = e^{-x}(2cos3x+\frac{1}{3}sin3x) $')

x = numpy.linspace(0, 2*numpy.pi, 10000)
y = pB(x)
Graph(x, y, r'$ y = e^{-x}(cos3x+\frac{1}{3}sin3x) $')

x = numpy.linspace(0, 2*numpy.pi, 10000)
y = pC(x)
Graph(x, y, r'$ y = e^{-x}+e^x(cosx+sinx)$')

x = numpy.linspace(0, 1, 10000)
y = pD(x)
Graph(x, y, r'$ y = e^{4x}+e^{-4x}-\frac{1}{8}e^{-4x}x$')

x = numpy.linspace(0, 4*numpy.pi, 10000)
y = pE(x)
Graph(x, y, r'$ y = cos2x+\frac{1}{4}xsin2x$')

x = numpy.linspace(0, 1, 10000)
y = pF(x)
Graph(x, y, r'$ y = x+x^2+xe^x$')

plt.show()