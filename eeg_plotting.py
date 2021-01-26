# import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('macosx')  # or can use 'TkAgg', whatever you have/prefer
import plotly.graph_objects as go


# %%
def create_plot_of_EEG(a, fs, t, V):
    # Create figure

    # set layout
    layout = go.Layout(
        title="EEG - Voltage series - %s - %s" % (a.abfFileComment, a.abfFilePath[-12:]),  # set title
        plot_bgcolor="#FFF",  # Sets background color to white
        hovermode='x',
        hoverdistance=10,
        spikedistance=1000,
        xaxis=dict(
            title="time (seconds)",
            linecolor="#BCCCDC",  # Sets color of X-axis line
            showgrid=False,  # Removes X-axis grid lines
            # rangeslider=list(),

            # format spikes
            showspikes=True,
            spikethickness=2,
            spikedash='dot',
            spikecolor="#999999",
            spikemode='across'
        ),
        yaxis=dict(
            title="voltage",
            linecolor="#BCCCDC",  # Sets color of Y-axis line
            showgrid=False,  # Removes Y-axis grid lines
            fixedrange=False,
            rangemode='normal'
        )
    )

    fig = go.Figure(data=go.Scatter(x=list(t[::10]), y=list(V[0][::10]), line=dict(width=0.95)),
                    # downsampling data by 10,
                    layout=layout)

    # fig.update_traces(hovertemplate=None)

    # fig.add_trace(
    #     go.Scatter(x=list(t[::10]), y=list(V[0][::10]), line=dict(width=0.75)))  # downsampling data by 10

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


# %% power spectrum of the EEG
import matplotlib.pyplot as plt
import numpy as np


def power_spectrum(a, fs, t, V, start=None, stop=None):
    # create a power spectrum of selected data
    if start & stop:
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
