import pandas as pd
import plotly.graph_objs as go
from scripts.googleAPI import SheetsAPI
import plotly.offline as pyoff


def get_timeseries():
    # Read data
    sheet_id = "1RORhvV7Lb1X3o-qPHawxfcxxgRxI6Zgt_Aq9Jog1RYE"
    sheet_range = "A:A"
    api = SheetsAPI()
    df = api.get_df(sheet_id, sheet_range)
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
    fig = go.Figure(data=data, layout=layout)

    return pyoff.plot(fig,
                      show_link=False,
                      output_type="div",
                      include_plotlyjs=False)


def get_week():
    # Read data
    df = pd.read_csv("./scratch/test_data/timeseries_test_data.csv")
    df.DateTime = pd.to_datetime(df.DateTime)

    days = [
        df[df.DateTime.dt.weekday == 0].groupby(df.DateTime.dt.hour).size(),
        df[df.DateTime.dt.weekday == 1].groupby(df.DateTime.dt.hour).size(),
        df[df.DateTime.dt.weekday == 2].groupby(df.DateTime.dt.hour).size(),
        df[df.DateTime.dt.weekday == 3].groupby(df.DateTime.dt.hour).size(),
        df[df.DateTime.dt.weekday == 4].groupby(df.DateTime.dt.hour).size(),
        df[df.DateTime.dt.weekday == 5].groupby(df.DateTime.dt.hour).size(),
        df[df.DateTime.dt.weekday == 6].groupby(df.DateTime.dt.hour).size()
    ]

    data = []
    for d in days:
        # Add to trace
        trace = go.Scatter(
            x=d.index,
            y=d,
            mode="lines"
        )
        data.append(trace)

    # Create layout
    layout = dict(
        title='Scatter',
        xaxis=dict()
    )

    fig = go.Figure(data=data, layout=layout)

    return pyoff.plot(fig,
                      show_link=False,
                      output_type="div",
                      include_plotlyjs=False)

