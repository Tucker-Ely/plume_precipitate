# Plume_Precip: precipitation energetics in hydrothermal plumes
# Copyright (C) 2022  Tucker Ely  (GNU GPLv3)
"""Define logK constraints for minerals"""

from os.path import realpath
# from csv import reader
import pandas as pd


class db_info:
    """ load the worm portal database being used """
    def __init__(self, worm_csv):
        self.dir = realpath(worm_csv)
        self.dat = pd.read_csv(self.dir)

    def get_elements(self, load_minerals):
        """ determine list of elements implied by mineral list"""
        fluid_species = []  # unique aqueous sp/gasses among all dissolution rxns
        minerals = {}  # dict[minal_name] = mineral_instance
        for sp in load_minerals:
            rxn = list(self.dat[(self.dat['name'] == sp)]['dissrxn'])[0]
            minerals[sp] = mineral(rxn)
            fluid_species.extend([_ for _ in minerals[sp].sp if _ != sp])
        fluid_species = list(set(fluid_species))
        return minerals, fluid_species

    def list_sp(self):
        """ which speies are in the loaded worm database"""
        return list(self.dat['name'])


class mineral:
    """ mineral instances loaded from worm style csv file"""
    def __init__(self, diss_rxn):
        diss_rxn = diss_rxn.split()
        self.name = diss_rxn[1]
        self.sto = [float(_) for _ in diss_rxn[::2]]
        self.sp = diss_rxn[1::2]


class env:
    """establish mixing environemnt that mienrals will participate in"""
    pass
