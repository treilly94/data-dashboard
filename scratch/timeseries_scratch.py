import pandas as pd
import plotly.offline as pyoff
import plotly.graph_objs as go

# Read data
df = pd.read_csv("./test_data/timeseries_test_data.csv")
df.DateTime = pd.to_datetime(df.DateTime)

# Identify days
df["Weekday"] = df.DateTime.dt.weekday
df["Weekday_name"] = df.DateTime.dt.weekday_name

# Get days
days = [df[df.Weekday == d] for d in range(7)]

# Make Scatterplot
data = []
for dayDf in days:
    trace = go.Scatter(
        x=dayDf.DateTime.dt.date,
        y=dayDf.DateTime.dt.hour,
        mode="lines",
        text=dayDf.DateTime.dt.weekday_name
    )
    data.append(trace)

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
    )
)

print(days[0])

pyoff.plot(
    dict(data=data, layout=layout)
)
