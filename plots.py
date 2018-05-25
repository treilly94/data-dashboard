import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyoff


def get_timeseries():
    # Read data
    df = pd.read_csv("./scratch/test_data/timeseries_test_data.csv")
    df.DateTime = pd.to_datetime(df.DateTime)

    # Make Scatterplot
    data = [
        go.Scatter(
            x=df.DateTime.dt.date,
            y=df.DateTime.dt.hour,
            mode="lines",
            text=df.DateTime.dt.weekday_name
        )
    ]

    layout = dict(
        title='Scatter',
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(),
            type='date'
        ),
        yaxis=dict(
            title='time'
        )
    )

    return pyoff.plot(dict(data=data, layout=layout),
                      show_link=False,
                      output_type="div",
                      include_plotlyjs=True)
