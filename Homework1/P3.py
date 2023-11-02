import numpy
import matplotlib.pyplot as plt

X = numpy.arange(-5, 5, 0.5)
Y = numpy.arange(-5, 5, 0.5)

x, y = numpy.meshgrid(X, Y)

def Graph(id,x, y, dx, dy):
    plt.subplot(2,2,id)
    plt.quiver(x, y, dx, dy)
    plt.xlabel('x', loc = 'right')
    plt.ylabel('y', loc = 'top', rotation = 0)
    plt.text(0, 0, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.5, wrap = True, fontsize = 25)

    plt.grid()

    

def a():
    dy = x + y 
    dx = 1
    norm = numpy.sqrt(dx**2 + dy**2)
    dy = dy / norm
    dx = dx / norm
    Graph(1,x, y, dx, dy)
    plt.title('y\' = x + y')

def b():
    dy = x-y
    dx = 1
    norm = numpy.sqrt(dx**2 + dy**2)

    dy = dy / norm
    dx = dx / norm

    Graph(2,x, y, dx, dy)
    plt.title('y\' = x - y')

def c():
    dy  = x*y 
    dx = 1
    norm = numpy.sqrt(dx**2 + dy**2)

    dy = dy / norm
    dx = dx / norm

    Graph(3,x, y, dx, dy)   
    plt.title('y\' = xy')

def d():
    dy = numpy.sin(x) * numpy.cos(y)
    dx = 1
    norm = numpy.sqrt(dx**2 + dy**2)

    dy = dy / norm
    dx = dx / norm

    Graph(4,x, y, dx, dy)
    plt.title('y\' = sin(x) cos(y)')

a()
b()
c()
d()
plt.suptitle('Direction Field')


plt.show()