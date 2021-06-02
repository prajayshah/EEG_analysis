import pyabf
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt  # - commented out because it causes major problems with plotly imports i think


# %% open a selection dialog to retrieve EEG file names to analyse, then read this file using pyabf

def open_selection_abf(
        initial_location='/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG'):
    # open a selection dialog to retrieve EEG file names to analyse
    root = tk.Tk()
    root.withdraw()

    # filez = filedialog.askopenfilenames(initialdir='/Volumes/Extreme SSD/Exp 2020.1T_KainicAcidOptogenetics/247EEG', parent=root, title='Choose files')
    filez = filedialog.askopenfilenames(initialdir=initial_location, parent=root, title='Choose files')
    fpath = list(root.tk.splitlist(filez))
    print(fpath)

    return fpath


# file_path = '/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2018-2019/Epilepsy model project/EEG recordings/2019_09_13_0002.abf'
# fpath = file_path

def load_abf(initial_location=None):
    '''
    :param initial_loc: str; where would you like the selection dialog to open first.
    :return: a bunch of variables containing data from the ABF file. sorry for not providing more details on what it returns.

    example use of the load_abf function:

    a, fs, t, V = load_abf('/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG')

    '''

    # make file selection for abf file
    fpath = open_selection_abf(initial_location=initial_location)
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

# %% PLOTTING FUNCTIONS
def eeg_plot(t, V, fs, ymin=-3, ymax=3, start=None, finish=None, linewidth=0.5, extend=1, title=None):
    '''
    :param t: timerange of data
    :param V: Voltage response of data
    :param start: start time of plot (in seconds)
    :param finish: finish time of plot (in seconds)
    :return:
    '''

    if start == None and finish == None:
        start = 0
        finish = t[-1].__int__()

    # subset data for plotting
    x = t[start * fs:finish * fs]
    y = V[0][start * fs:finish * fs]

    # plot
    w, h = plt.figaspect((5. * (finish - start) / 1000) ** -1)
    # plt.figure(figsize=((5. * (finish-start)/1000), 5))
    plt.figure(figsize=(extend * w + 2, h + 2))
    plt.style.use('fivethirtyeight')
    plt.margins(x=0)
    line = plt.plot(x, y)
    plt.setp(line, linewidth=linewidth)
    plt.ylim([ymin, ymax])
    plt.xticks(np.arange(int(min(t)), int(max(t) + 1), 5.0))
    if title:
        plt.title(title)
    plt.show()


# power spectrum of the EEG
def run_spectrum(a, fs, t, V, start=None, stop=None):
    # create a power spectrum of selected data
    if start or stop:
        t_sub = np.where((t > 0) & (t < 115))
        V = V[0][t_sub]

    powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(V, Fs=fs,
                                                                   vmin=-60)
    # freq_slice = np.where((freqenciesFound >= 2) & (freqenciesFound <= 100))
    # powerSpectrum = powerSpectrum[freq_slice, :][0]
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.ylim([0, 200])
    # plt.xlim([25, 90])
    plt.colorbar()
    plt.show()
