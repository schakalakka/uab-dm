import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

from problems import models

# choose herre the system of odes from the models.py file
model = models.chemical_oscillations

x_low = 0
x_high = 3.5
y_low = 1
y_high = 13

# MESH
x = np.linspace(x_low, x_high, 8)
y = np.linspace(y_low, y_high, 8)
t = 0
X, Y = np.meshgrid(x, y)
u, v = np.zeros(X.shape), np.zeros(Y.shape)
NI, NJ = X.shape
for i in range(NI):
    for j in range(NJ):
        x = X[i, j]
        y = Y[i, j]
        yprime = model([x, y], t)
        u[i, j] = yprime[0]
        v[i, j] = yprime[1]
Q = plt.quiver(X, Y, u, v, color='r')

# CURVES
trajectories1 = [(0, 0), (0, 0.8), (0.8, 0), (0.2, 0.2), (0.7, 0.7), (0.7, 0.2), (0.2, 0.7), (0.3, 0.2), (0.2, 0.3),
                 (0.7, 0.9), (0.9, 0.7)]
# trajectories2 = [(2, 5), (3, 5), (2.1, 5)]
a = 10
b = 3*a/5-25/a+0.1
trajectories2 = [(3.2, 10)]
for s0 in trajectories2:
    tspan = np.linspace(0, 200, 1600)
    ys = odeint(model, s0, tspan, mxstep=5000000)
    # plt.plot(ys[:, 0], ys[:, 1], 'b-')  # path
    plt.quiver(ys[:-1, 0], ys[:-1, 1], ys[1:, 0] - ys[:-1, 0], ys[1:, 1] - ys[:-1, 1], width=0.004, scale=1,
               scale_units='xy', angles='xy', color='b')
    plt.plot([ys[0, 0]], [ys[0, 1]], 'go')  # start
    # plt.plot([ys[-1, 0]], [ys[-1, 1]], 'ys')  # end

# plt.plot(np.linspace(0, 1, 11), [1 - x for x in np.linspace(0, 1, 11)], 'y--')


a = 10
b = 3*a/5-25/a+1
# Nullclines
xspace =np.linspace(0.25, x_high, 30)
yspace = np.linspace(y_low, y_high, 30)
plt.plot(xspace, [(a-x)*(1+x*x)/(4*x) for x in xspace], 'k-', label='fas')
plt.plot(xspace, [1+x*x for x in xspace], 'k-')
# plt.plot([0.5]*2, [1,10], 'y--')
# plt.plot([3.5]*2, [1,10], 'y--')
# plt.plot([0.5, 3.5], [1]*2, 'y--')
# plt.plot([0.5, 3.5], [10]*2, 'y--')
plt.plot(a/5, 1+a*a/25, 'bs')
# plt.plot(3.5, 12, "$y' = 0$")


plt.grid(color='black', linestyle='--', linewidth=0.2)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Stable Spiral, $a=10, b=4.5>\\frac{3a}{5}-\\frac{25}{a}$')
# plt.xlim([loweraxelimit, upperaxelimit])
# plt.ylim([loweraxelimit, upperaxelimit])

# plt.show()
fig = plt.gcf()
fig.show()
fig.savefig('phaseportrait.png')

# line_chart = pygal.XY(dots_size=0.5)  # simple xy chart with line stroke
# line_chart.add(f'x', list(zip(t, s[:, 0])))
# line_chart.add(f'y', list(zip(t, s[:, 1])))
#
# line_chart.render_to_png(f'plot.png')
# line_chart.render_in_browser()
