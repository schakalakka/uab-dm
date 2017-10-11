import pygal
import numpy as np


n = 100

def plot(r, inits):
    line_chart = pygal.XY()
    line_chart.title = f"{r}"
    line_chart.y_labels = np.arange(0, 1.1, 0.1)
    # line_chart.x_labels = np.arange(0, n+1)
    for initial_value in inits:
        arr = np.zeros(n)
        arr[0] = initial_value
        for i in range(1, n):
            arr[i] = r * arr[i - 1] * (1 - arr[i - 1])
        line_chart.add(f'r={r}, x_2={initial_value}', list(zip(range(n), arr)))
    # line_chart.render_to_file(f'plot_{r}_{l}.svg')
    # line_chart.render_to_png(f'plot_{r}_{l}.png')
    line_chart.render_in_browser()



#exercise 3
R = [0.5, 2, 3.2, 3.4, 4]
inits = [0.2, 0.4]

for r in R:
    plot(r, inits)

#exercise 4
inits_list = ([0.2001, 0.2002], [0.4004, 0.4003], [0.40000004, 0.40000003], [0.4000000000000004, 0.4000000000000003])
for init in inits_list:
    plot(4, init)




