# import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.use('macosx')  # or can use 'TkAgg', whatever you have/prefer
import plotly.graph_objects as go


# %%
def create_plot(a, fs, t, V):
    # Create figure

    # set layout
    layout = go.Layout(
        title="EEG - Voltage series - %s - %s" % (a.abfFileComment, a.abfFilePath[-12:]),  # set title
        plot_bgcolor="#FFF",  # Sets background color to white
        hovermode='x',
        hoverdistance=10,
        spikedistance=1000,
        xaxis=dict(
            title="time",
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
            title="price",
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
