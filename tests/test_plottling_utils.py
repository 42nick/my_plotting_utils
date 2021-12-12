import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from my_plotting_utils.plotting_utils import PlottingUtils as pu


def test_PlottingUtils_getFigure():

    fig = pu.getFigure()
    assert isinstance(fig, Figure)


def test_PlottingUtils_setPlot():

    plt.plot([1, 2, 3], [1, 2, 2])

    xtitle = "my_xtitle"
    pu.setPlot(x=xtitle)

    ax = plt.gca()

    assert ax.xaxis.get_label().get_text() == xtitle
