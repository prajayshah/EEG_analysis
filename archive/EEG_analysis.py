import pyabf
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# ----------------------------------------------------------------------------------------------------------------------
# Load up the abf file into python
# ----------------------------------------------------------------------------------------------------------------------

# %% open a selection dialog to retrieve EEG file names to analyse
root = tk.Tk()
root.withdraw()

# filez = filedialog.askopenfilenames(initialdir='/Volumes/Extreme SSD/Exp 2020.1T_KainicAcidOptogenetics/247EEG', parent=root, title='Choose files')
filez = filedialog.askopenfilenames(
    initialdir='/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2020/Exp 2020.1T/2020-10-19_OptoEEG',
    parent=root, title='Choose files')
fpath = list(root.tk.splitlist(filez))
print(fpath)


#


# file_path = '/Users/prajayshah/OneDrive - University of Toronto/UTPhD/2018-2019/Epilepsy model project/EEG recordings/2019_09_13_0002.abf'
# fpath = file_path

# Load up abf file with pyABF

def load_abf(fpath=fpath):
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

    return a, fs, t, V


if len(fpath) == 1:
    a, fs, t, V = load_abf(fpath[0])


# %% plot EEG
# subset data and plot
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


eeg_plot(t, V, fs=fs, linewidth=0.5, ymin=-1.5, ymax=1.5, extend=10, title=a.abfFileComment,
         start=0,
         finish=600)

# %% subset of EEG data
t_sub = np.where((t > 0) & (t < 115))
V_sub = [V[0][t_sub]]

eeg_plot(t[t_sub], V_sub, fs=fs, linewidth=1.5, ymin=-1.5, ymax=1.5,
         extend=20, title=a.abfFileComment)

# create a power spectrum of selected data
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(V_sub[0], Fs=fs,
                                                               vmin=-60)
# freq_slice = np.where((freqenciesFound >= 2) & (freqenciesFound <= 100))
# powerSpectrum = powerSpectrum[freq_slice, :][0]
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.ylim([0, 200])
# plt.xlim([25, 90])
plt.colorbar()
plt.show()

# %% use plotly for plotting

import matplotlib as mpl

# import matplotlib.pyplot as plt
mpl.use('macosx')  # or can use 'TkAgg', whatever you have/prefer
import plotly.graph_objects as go

import pandas as pd

# %%

# Load data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
df.columns = [col.replace("AAPL.", "") for col in df.columns]

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.High)))

# Set title
fig.update_layout(
    title_text="Time series with range slider and selectors"
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

fig.show()

# go.FigureWidget(fig)


# %%
# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(t), y=list(V[0])))

# Set title
fig.update_layout(
    title_text="EEG - Voltage series - %s - %s" % (a.abfFileComment, a.abfFilePath[-12:])
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="linear"
    )
)

fig.show()

# go.FigureWidget(fig)
