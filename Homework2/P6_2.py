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
def Graph(x, y, title, color = 'blue'):
    global count
    plt.subplot(2, 2, count + 1)
    plt.plot(x, y, color = color, label = title)
    plt.xlabel('x', loc = 'right')
    plt.ylabel('y', loc = 'top', rotation = 0)
    plt.title(title)
    x_center = (x[0] + x[-1]) / 2
    y_center = max(y) - (max(y) - min(y)) / 2
    plt.text(x_center, y_center, 'CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
    plt.legend()
    count += 1
    
    #plt.show()

def A(t): # K = 14
    return exp(-0.1*t)*(53.823*cos(sqrt(279)/10*t)+6.806*sin(sqrt(279)/10*t)) + 80/7

def B(t): # K = 8.5
    return exp(-0.1*t)*(48.987*cos(1.3*t)-50.891*sin(1.3*t)) + 18.824

def C(t): # K = 10.7
    return exp(-0.1*t)*(56.913*cos(1.45*t) - 26.533*sin(1.45*t)) + 14.953

def D(t): # K = 16.4
    return exp(-0.1*t)*(43.99*cos(1.81*t)+23.43*sin(1.81*t)) + 9.756


t = numpy.linspace(0, 60, 1000)
y = B(t)
Graph(t, y, r'$ K = 8.5 $')

y = C(t)
Graph(t, y, r'$ K = 10.7 $', color = 'red')

y = A(t)
Graph(t, y, r'$ K = 14 $', color = 'green')

y = D(t)
Graph(t, y, r'$ K = 16.4 $', color = 'black')



#x_center = 30
#y_center = max(y) - (max(y) - min(y)) / 2
#plt.text(x_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
plt.show()