# load and plot an EEG recording file

from EEG_utils import *
from EEG_plotly import *


# %%

def run_EEG_load_plot(initial_location):
    """
    :param initial_location: str; where would you like the selection dialog to open first.

    example use:
        a, fs, t, V =
            run_EEG_load_plot(initial_location=
                '/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')

    """

    a, fs, t, V = load_abf(initial_location=initial_location)
    create_plot_of_EEG(a, fs, t, V)

    return a, fs, t, V


a, fs, t, V = run_EEG_load_plot(
    initial_location='/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')
