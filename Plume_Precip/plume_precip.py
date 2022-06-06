# Plume_Precip: precipitation energetics in hydrothermal plumes
# Copyright (C) 2022  Tucker Ely  (GNU GPLv3)
"""Define logK constraints for minerals"""

from plume_precip import (
    constants,
    mineral_logk,
    visualize
)


def main():
    print(constants.b)
    print(visualize.a)
    print(mineral_logk.logk)


if __name__ == "__main__":
    main()
