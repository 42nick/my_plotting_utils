from typing import Optional

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib

matplotlib.use("Agg")


class PlottingUtils:
    @staticmethod
    def getFigure(figsize=(16, 9), **kwargs) -> Figure:
        return plt.figure(figsize=figsize, **kwargs)

    @staticmethod
    def setPlot(x=None, y=None, t=None, xlim=None, ylim=None, leg=None):
        ax = plt.gca()
        ax.set_axisbelow(True)
        ax.minorticks_on()
        ax.grid(linestyle="-", linewidth="0.5", color="#dddddd", which="minor")
        ax.grid(linestyle="--", linewidth="0.7", color="#999999", which="major")
        ax.set_xlabel(x) if x is not None else None
        ax.set_ylabel(y) if y is not None else None
        ax.set_title(t) if t is not None else None
        ax.set_xlim(xlim) if xlim is not None else None
        ax.set_ylim(ylim) if ylim is not None else None
        ax.legend() if leg else None


MISSING = object()  # this is a sentinal


def printSmth(smt_to_print: Optional[int] = MISSING):

    if smt_to_print is MISSING:
        print("x IS MISSING")
    elif smt_to_print is None:
        print("x IS None")
    else:
        print(smt_to_print)
