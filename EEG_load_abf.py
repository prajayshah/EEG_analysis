import pyabf
import numpy as np
import tkinter as tk
from tkinter import filedialog


# %% open a selection dialog to retrieve EEG file names to analyse, then read this file using pyabf

def open_selection_abf(
        initial_loc='/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG'):
    # open a selection dialog to retrieve EEG file names to analyse
    root = tk.Tk()
    root.withdraw()

    # filez = filedialog.askopenfilenames(initialdir='/Volumes/Extreme SSD/Exp 2020.1T_KainicAcidOptogenetics/247EEG', parent=root, title='Choose files')
    filez = filedialog.askopenfilenames(initialdir=initial_loc, parent=root, title='Choose files')
    fpath = list(root.tk.splitlist(filez))
    print(fpath)

    return fpath


# file_path = '/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2018-2019/Epilepsy model project/EEG recordings/2019_09_13_0002.abf'
# fpath = file_path

def load_abf(initial_loc=None):
    '''
    :param initial_loc: str; where would you like the selection dialog to open first.
    :return: a bunch of variables containing data from the ABF file. sorry for not providing more details on what it returns.

    example use of the load_abf function:

    a, fs, t, V = load_abf('/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')

    '''

    # make file selection for abf file
    fpath = open_selection_abf(initial_loc=initial_loc)
    if len(fpath) == 1:
        fpath = fpath[0]  # select the first file path in the list (there should only be one anyways)
        # Load up abf file with pyABF
        print('Loading %s' % fpath)

        a = pyabf.ABF(fpath)
        fs = a.dataRate  # sampling frequency
        V = a.data
        t = np.arange(0, len(V[0])) * (
                    1.0 / fs)  # length of the data, converted to seconds by dividing by the sampling frequency
        print('ABF File Comment: ', a.abfFileComment)
        print('Sampling rate: ', fs)
        print('length of recording (seconds): ', t[-1])
        print('number of datapoints: ', len(V[0]))

    else:
        TypeError('something is wrong with your fpath selection !!!')

    return a, fs, t, V

# if len(fpath)==1:
#     a, fs, t, V = load_abf('/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')

# example use of the load_abf function
# a, fs, t, V = load_abf('/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')
