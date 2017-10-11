import pygal
import numpy as np
import random

###
# orbit diagramm for logistics map for 0 < r <= 4
###
rs = np.linspace(0.1, 4, 200)
data = []
for r in rs:
    temp_data = []
    # try several times for random starting values
    for j in range(5):
        x = random.random()
        for i in range(50):  # get rid of transient values
            x = r * x * (1 - x)
        for i in range(200):  # now look at the behavior after the initial transient values
            x = r * x * (1 - x)
            if x not in temp_data:
                temp_data.append(x)
    data.extend([(r, x) for x in temp_data])  # store each value in the orbit corresponding to a r

plotfilename = 'logisticsmap'
l_chart = pygal.XY(dots_size=0.5, stroke=False)  # simple xy chart without line stroke
l_chart.title = 'Orbit diagram of Logistics map'
l_chart.add('', data)
l_chart.render_to_file(f'{plotfilename}.svg')
l_chart.render_to_png(f'{plotfilename}.png')
l_chart.render_in_browser()
