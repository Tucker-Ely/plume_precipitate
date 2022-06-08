# Plume_Precip: precipitation energetics in hydrothermal plumes
# Copyright (C) 2022  Tucker Ely  (GNU GPLv3)
""" visualize mienral data against mixing environemnt """

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

font = {'family': 'andale mono', 'size': 8}
matplotlib.rc('font', **font)
matplotlib.rcParams['axes.edgecolor'] = '#000000'
matplotlib.rcParams['axes.linewidth'] = 0.5
matplotlib.rcParams['axes.labelsize'] = 8
matplotlib.rcParams['axes.titlesize'] = 8
matplotlib.rcParams['figure.titlesize'] = 8
matplotlib.rcParams['xtick.color'] = '#000000'
matplotlib.rcParams['ytick.color'] = '#000000'
matplotlib.rcParams['axes.labelcolor'] = '#000000'
matplotlib.rcParams['legend.frameon'] = False
matplotlib.rcParams['savefig.transparent'] = True


def power_law(x, a, b):
    return a * np.power(x, b)


def plt_plot(ax, df, x, y, color, lw=0.5):
    """
    plot subset of marhys database with style (mk=marker, sz=marker size,
        fc=face color, ec=edge color, lw-edge line width)

    The subset plotted is the group (groupby), within the column (col_name) on
        the datafram df.

    z order refers to the plotting layer relative to other groups which may
        be plotted ont the same ax, which is exstablished outside this
        function prioir to its first calling.
    """
    ax.plot(x,
            y,
            c=color,
            linewidth=lw,
            data=df
            # zorder=zorder
            )


    # def plot_logK(env, sup_minerals):
    #     """ plot mienral data against mixing environemnt"""

    #     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 9), tight_layout=True)
    #     ax2.axis('off')

    #     x = env.log_xi_steps
    #     # ### solve logK at deisred T steps
    #     for sp in sup_minerals.keys():
    #         x, y = ['T_cel', 'LogK']
    #         df = sup_minerals[sp].df
    #         df = df[df['P_bar'] == 500][[x, y]]
    #         plt_plot(ax1, df, x, y, 'black', lw=0.5)
    #     plt.show()


def plot_logQ(self, ax):
    """ plot mienral data against mixing environemnt"""
    x = self.log_hf_sw
    y = self.Q['pyrite']
    # ax.plot(x, y, linewidth=0.5)
    ax.scatter(x, y, s=0.2, c='black', marker='o')


def plot_logK(self, ax, sup_minerals):
    # ### solve logK at deisred T steps
    x, y = ['T_cel', 'LogK']
    df = sup_minerals['pyrite'].df
    df = df[df['P_bar'] == 500][[x, y]]
    ax.plot(x, y, data=df, linewidth=0.5)
    # plt_plot(ax1, df, x, y, 'black', lw=0.5)


def plot_aq(self, ax):
    """ plot mienral data against mixing environemnt"""
    # x = env.xi_steps
    x = self.log_hf_sw

    # ### solve logK at deisred T steps
    for sp in self.fluid_species:
        y = self.fluid_values[sp]
        ax.plot(x, y, linewidth=0.5)
        # ax.scatter(x, y, s=0.2, c='black', marker='o')



def test_eq(env, sup_minerals):

    # x = env.hf_sw_steps

    x = np.linspace(start=1, stop=1000, num=100)
    y = power_law(x, 1, 0.5)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 9), tight_layout=True)
    ax2.axis('off')

    plt.show()

    # ### everything is a function of x

    # ### (1) calculate y from x

    # ### (2) fit curve to y

    # ### (3) check scatter versus curve for fit
