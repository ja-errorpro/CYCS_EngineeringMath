import numpy
import matplotlib.pyplot as plt
import scipy.integrate as integrate

sin = numpy.sin
cos = numpy.cos
sqrt = numpy.sqrt
exp = numpy.exp
pi = numpy.pi

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

G = 32 # 32 ft/s^2
m = 5 # 5 slugs 
count = 0

def one_order_ode(t, y):
    dy1 = y[1] # dy1 = y1'
    dy2 = (m*G - K*y[0] - dy1)/m # my'' + y' + Kx = mG, y'' = (mG - y' - Kx)/m
    return [dy1, dy2]

def solve():
    global count
    plt.subplot(2, 2, count + 1)
    t = numpy.linspace(0, 60, 1000) # 0 <= t <= 60
    y0 = [0, 67.32] # y(0) = 0, y'(0) = 67.32
    y = integrate.odeint(one_order_ode, y0, t, tfirst=True) # solve the ODE
    y1, = plt.plot(t,y[:,0],label='y')
    #y1_1, = plt.plot(t,y[:,1],label='y\'')
    #plt.legend(handles=[y1,y1_1])
    plt.xlabel('t', loc = 'right')
    plt.ylabel('y', loc = 'top', rotation = 0)
    plt.title('K = ' + str(K))
    t_center = (t[0] + t[-1]) / 2
    y_center = max(y[:,0]) - (max(y[:,0]) - min(y[:,0])) / 2
    plt.text(t_center, y_center, 'Copyright@CompileErr0r(11127137)', ha = 'center', va = 'center', rotation = 15, alpha = 0.2, wrap = True, fontsize = 25)
    count += 1

K = 8.5

solve()

K = 10.7

solve()

K = 14

solve()

K = 16.4

solve()

plt.show()

