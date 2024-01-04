import numpy
import matplotlib.pyplot as plt

sin = numpy.sin
cos = numpy.cos
sqrt = numpy.sqrt
exp = numpy.exp
pi = numpy.pi

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
count = 0
def Graph(x, y, title):
    global count
    plt.subplot(2, 2, count + 1)
    plt.plot(x, y)
    plt.xlabel('x', loc = 'right')
    plt.ylabel('y', loc = 'top', rotation = 0)
    plt.title(title)
    x_center = (x[0] + x[-1]) / 2
    y_center = max(y) - (max(y) - min(y)) / 2
    plt.text(x_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
    #plt.show()
    count += 1

def pA_charge(x):
    return numpy.exp(-10*x)*(3/2050*numpy.cos(30*x)+7/1025*numpy.sin(30*x)) - 3/2050*cos(60*x) - 13/4100*sin(60*x)

def pA_current(x):
    return -10*numpy.exp(-10*x)*(3/2050*numpy.cos(30*x)+7/1025*numpy.sin(30*x)) + numpy.exp(-10*x)*(-90/2050*numpy.sin(30*x)+210/1025*numpy.cos(30*x)) + 180/2050*sin(60*x) - 780/4100*cos(60*x)

def pB_charge(x):
    return 50*cos(sqrt(1000)*x)

def pB_current(x):
    return -50*sqrt(1000)*sin(sqrt(1000)*x)


x = numpy.linspace(0, 4*pi, 100)
y = pA_charge(x)
Graph(x, y, r'$ y = e^{-10x}(\frac{3}{2050}cos30x+\frac{7}{1025}sin30x)-\frac{3}{2050}cos60x-\frac{13}{4100}sin60x$')

x = numpy.linspace(0, 4*pi, 100)
y = pA_current(x)
Graph(x, y, r'$ y = -10e^{-10x}(\frac{3}{2050}cos30x+\frac{7}{1025}sin30x)+e^{-10x}(-\frac{90}{2050}sin30x+\frac{210}{1025}cos30x)+\frac{180}{2050}sin60x-\frac{780}{4100}cos60x$')

x = numpy.linspace(0, 4*pi, 100)
y = pB_charge(x)
Graph(x, y, r'$ y = 50cos(\sqrt{1000}x)$')

x = numpy.linspace(0, 4*pi, 100)
y = pB_current(x)
Graph(x, y, r'$ y = -50\sqrt{1000}sin(\sqrt{1000}x)$')

plt.show()