import numpy
import matplotlib.pyplot as plt
from matplotlib import cm 
from mpl_toolkits.mplot3d import Axes3D

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

def Graph(x, y, z, title, xLabel, yLabel):
    fig = plt.figure(1)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    plt.xlabel(xLabel, loc = 'right')
    plt.ylabel(yLabel, loc = 'top', rotation = 0)
    plt.title('3D Plot of f(x,y) = '+title)
    ax.text2D(0.05, 0.95, "Copyright@CompileErr0r(11127137)", transform=ax.transAxes)
    #plt.show()

    plt.figure(2)
    plt.contour(x, y, z, 30)
    plt.xlabel(xLabel, loc = 'right')
    plt.ylabel(yLabel, loc = 'top', rotation = 0)
    plt.title('Contour Plot of '+title)
    x_center = (x[0][0] + x[-1][-1]) / 2
    y_max = max( [max(i) for i in y] )
    y_min = min( [min(i) for i in y] )
    y_center = y_max - (y_max - y_min) / 2
    plt.text(x_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
    plt.show()

X = numpy.linspace(-2, 2, 100)
Y = numpy.linspace(-2, 2, 100)
x,y = numpy.meshgrid(X, Y)
z = x*(y**2) + 4*x*y

Graph(x, y, z, r'$ xy^2 + 4xy$ ', 'x', 'y')

X = numpy.linspace(0, 2, 100)
Y = numpy.linspace(0, 2, 100)
x,y = numpy.meshgrid(X, Y)
z = x**2 + x*numpy.exp(y)

Graph(x, y, z, r'$ x^2 + xe^y $', 'x', 'y')

X = numpy.linspace(0, 2*numpy.pi, 1000, endpoint = False)
Y = numpy.linspace(0, 2*numpy.pi, 1000, endpoint = False)
x,y = numpy.meshgrid(X, Y)
z = y**2 * numpy.exp(y) * numpy.sin(x)

Graph(x, y, z, r'$ y^2e^ysin(x) $', 'x', 'y')

X = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 100)
Y = numpy.linspace(-2*numpy.pi, 2*numpy.pi, 100)
x,y = numpy.meshgrid(X, Y)
z = x * numpy.sin(y) + y * numpy.cos(x) - 0.5 * y**2

Graph(x, y, z, r'$ xsin(y) + ycos(x) - \frac{1}{2}y^2 $', 'x', 'y')
