import pygal
import numpy as np
import random

###
# bifurcation diagramm for 0 < µ <=4
###
mus = np.linspace(0.1, 4, 200)
data = []
for mu in mus:
    temp_data = []
    # try several times for random starting values
    for j in range(5):
        x = random.random() * 10
        for i in range(50):  # get rid of transient values
            x = x * np.exp(mu * (1 - x))
        for i in range(200):  # now look at the behavior after the initial transient values
            x = x * np.exp(mu * (1 - x))
            if x not in temp_data:
                temp_data.append(x)
    data.extend([(mu, x) for x in temp_data])  # store each value in the orbit corresponding to a r

plotfilename = 'bifurcation'
xy_chart = pygal.XY(dots_size=0.5, stroke=False)  # create a simple xy chart without line strokes
xy_chart.title = 'Bifurcation diagram'
xy_chart.add('', data)
xy_chart.render_to_file(f'{plotfilename}.svg')
xy_chart.render_to_png(f'{plotfilename}.png')
xy_chart.render_in_browser()
