import pygal
import numpy as np

###
# plot a general overview for different µ
# µ_1= 0.5, µ_2 = 1, µ_3 = 2, µ_4=3, µ_5=4
# additional plot f(x) = x for fixed points
###

plotfilename = 'general_overview'
line_chart = pygal.XY(dots_size=0.5)  # create a simple xy-plot with a line stroke
line_chart.title = f"Plot for different µ for a 'general' overview"

last_x_val = 4
x_values = np.linspace(0, last_x_val, last_x_val * 40 + 1)  # computation/grid density
line_chart.add('µ=0.5', list(zip(x_values, [x * np.exp(0.5 * (1 - x)) for x in x_values])))
line_chart.add('µ=1', list(zip(x_values, [x * np.exp(1 * (1 - x)) for x in x_values])))
line_chart.add('µ=2', list(zip(x_values, [x * np.exp(2 * (1 - x)) for x in x_values])))
line_chart.add('µ=3', list(zip(x_values, [x * np.exp(3 * (1 - x)) for x in x_values])))
line_chart.add('µ=4', list(zip(x_values, [x * np.exp(4 * (1 - x)) for x in x_values])))
line_chart.add('f(x)=x', list(zip(x_values, x_values)))  # diagonal for better visualization fixed points
line_chart.x_labels = [x / 2 for x in range(0, last_x_val * 2 + 1)]
line_chart.render_to_file(f'{plotfilename}.svg')
line_chart.render_to_png(f'{plotfilename}.png')
line_chart.render_in_browser()
