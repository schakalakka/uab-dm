from config import *


def plot(plotfilename, datasets, labels):
    """
    Plot for a given filename, datasets and corresponding chart labels
    :param plotfilename:
    :param datasets:
    :param labels:
    :return:
    """
    line_chart = pygal.XY(dots_size=0.5)  # simple xy chart with line stroke
    line_chart.title = f"Fraction of sick people"
    for i, dataset in enumerate(datasets):
        line_chart.add(labels[i], list(zip(betas, dataset)))
    line_chart.x_labels = [x / 10 for x in range(0, 11)]
    line_chart.render_to_file(f'svgs/{plotfilename}.svg')
    line_chart.render_to_png(f'pngs/{plotfilename}.png')
    line_chart.render_in_browser()


def plot_all():
    with open('datasets/dataset_circular.pickle', 'rb') as f, open('datasets/dataset_non_circular.pickle', 'rb') as g:
        circular_data_set = pickle.load(f)
        non_circular_data_set = pickle.load(g)
    keys = [(N, T) for N in N_list for T in T_list]  # list of N,T pairs like [(150,250), (150, 300), ..]
    for i in range(len(circular_data_set)):
        N, T = keys[i]
        plot(f'plot_{N}_{T}', [circular_data_set[i], non_circular_data_set[i]],
             labels=[f'circular_{N}_{T}', f'non_circular_{N}_{T}'])
    plot('all_circular', circular_data_set, labels=[f'{N}_{T}' for N in N_list for T in T_list])


def plot_all_in_one():
    line_chart = pygal.XY(dots_size=0.5)  # simple xy chart with line stroke
    line_chart.title = f"Fraction of sick people"
    plotfilename = 'all'
    for N in N_list:
        for T in T_list:
            with open(f'datasets/dataset_{N}_{T}_circular.pickle', 'rb') as f, open(
                f'datasets/dataset_{N}_{T}_non_circular.pickle', 'rb') as g:
                circular_data_set = pickle.load(f)
                non_circular_data_set = pickle.load(g)
                line_chart.add(f'{N}_{T}_circular', list(zip(betas, circular_data_set)))
                line_chart.add(f'{N}_{T}_non_circular', list(zip(betas, non_circular_data_set)))
    line_chart.x_labels = [x / 10 for x in range(0, 11)]
    line_chart.render_to_file(f'svgs/{plotfilename}.svg')
    line_chart.render_to_png(f'pngs/{plotfilename}.png')
    line_chart.render_in_browser()

def plot_all_T_circular(N=150):
    line_chart = pygal.XY(dots_size=0.5)  # simple xy chart with line stroke
    line_chart.title = f"Fraction of sick people"
    plotfilename = f't_circular_{N}'
    for T in T_list:
        with open(f'datasets/dataset_{N}_{T}_circular.pickle', 'rb') as f:
            circular_data_set = pickle.load(f)
            line_chart.add(f'{N}_{T}_circular', list(zip(betas, circular_data_set)))
    line_chart.x_labels = [x / 10 for x in range(0, 11)]
    line_chart.render_to_file(f'svgs/{plotfilename}.svg')
    line_chart.render_to_png(f'pngs/{plotfilename}.png')
    line_chart.render_in_browser()


def plot_all_N_circular(T=250):
    line_chart = pygal.XY(dots_size=0.5)  # simple xy chart with line stroke
    line_chart.title = f"Fraction of sick people"
    plotfilename = f'n_circular_{T}'
    for N in N_list:
        with open(f'datasets/dataset_{N}_{T}_circular.pickle', 'rb') as f:
            circular_data_set = pickle.load(f)
            line_chart.add(f'{N}_{T}_circular', list(zip(betas, circular_data_set)))
    line_chart.x_labels = [x / 10 for x in range(0, 11)]
    line_chart.render_to_file(f'svgs/{plotfilename}.svg')
    line_chart.render_to_png(f'pngs/{plotfilename}.png')
    line_chart.render_in_browser()

# plot_all()
plot_all_in_one()
plot_all_T_circular()
plot_all_N_circular()