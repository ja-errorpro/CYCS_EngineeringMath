import numpy
import matplotlib.pyplot as plt

sin = numpy.sin
cos = numpy.cos
sqrt = numpy.sqrt
exp = numpy.exp
pi = numpy.pi

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def Graph(x, y, title, color = 'blue'):
    plt.plot(x, y, color = color, label = title)
   
    
    #plt.show()

def I1(t):
    return -10*exp(-5500*t)+10

def I2(t):
    return -10/11*exp(-5500*t)+10/11

def I3(t):
    return -100/11*exp(-5500*t)+100/11

t = numpy.linspace(0, 30, 1000)
y = I1(t)
Graph(t, y, r'$ I_1 = -10e^{-5500t}+10$')

t = numpy.linspace(0, 30, 1000)
y = I2(t)
Graph(t, y, r'$ I_2 = -\frac{10}{11}e^{-5500t}+\frac{10}{11}$', color = 'red')

t = numpy.linspace(0, 30, 1000)
y = I3(t)
Graph(t, y, r'$ I_3 = -\frac{100}{11}e^{-5500t}+\frac{100}{11}$', color = 'green')

plt.xlabel('x', loc = 'right')
plt.ylabel('y', loc = 'top', rotation = 0)
plt.title('Plot of $I_1$, $I_2$, $I_3$')
plt.legend()
x_center = 15
y_center = max(y) - (max(y) - min(y)) / 2
plt.text(x_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
plt.show()