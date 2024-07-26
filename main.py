import plotly.graph_objects as go

# Add data
month = [
    "January 2021",
    "February 2021",
    "March 2021",
    "April 2021",
    "May 2021",
    "June 2021",
    "July 2021",
    "August 2021",
    "September 2021",
    "October 2021",
    "November 2021",
    "December 2021",
]


month_alt = [
    "January 2021",
    "December 2021",
]
high_2014 = [28.8, 39.9]
low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

fig = go.Figure()
# Create and style traces
fig.add_trace(
    go.Scatter(
        x=month, y=low_2014, name="Low 2014", line=dict(color="royalblue", width=4)
    )
)
fig.add_trace(
    go.Scatter(
        x=month_alt,
        y=high_2014,
        name="High 2014",
        line=dict(color="firebrick", width=4),
    )
)

# Edit the layout
fig.update_layout(
    title="Average High and Low Temperatures in New York",
    xaxis_title="Month",
    yaxis_title="Temperature (degrees F)",
)


fig.show()
