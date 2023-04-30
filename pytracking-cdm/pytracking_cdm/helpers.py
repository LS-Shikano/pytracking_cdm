import matplotlib.pyplot as plt
import sys
sys.path.append('..')
from Sequencer import sequencer
from Distance_Matrix import calc_dist_matr


def viz(title, fig, nest_func):
    fig.tight_layout(pad=1)
    nest_func
    fig.suptitle(title, fontsize=16)
    plt.subplots_adjust(top=0.9)
    fig.set_size_inches(17, 8)


def scatter_func(axs,x_1, x_2, y_1, y_2, x_title, y_title):
    axs[0].scatter(x_1, x_2)
    axs[0].set_title(x_title)
    axs[1].scatter(y_1, y_2)
    axs[1].set_title(y_title)