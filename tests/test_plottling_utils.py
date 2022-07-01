import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from my_plotting_utils.plotting_utils import PlottingUtils as pu
from my_plotting_utils.plotting_utils import printSmth


def test_PlottingUtils_getFigure():

    fig = pu.getFigure()
    assert isinstance(fig, Figure)


def test_PlottingUtils_setPlot():

    plt.plot([1, 2, 3], [1, 2, 2])

    xtitle = "my_xtitle"
    pu.setPlot(x=xtitle)

    ax = plt.gca()

    assert ax.xaxis.get_label().get_text() == xtitle


def test_printSmth(capsys):
    printSmth()
    printSmth(smt_to_print=None)
    printSmth(smt_to_print="dfsf")

    captured = capsys.readouterr()

    expect = [
        "x IS MISSING\n",
        "x IS None\n",
        "dfsf\n",
    ]

    assert captured.out == "".join(expect)
