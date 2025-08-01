import pandas as pd
import plotly.express as px

ds = pd.read_csv("2.5_week.csv")
ds = ds.sort_values("time", ascending=True)
ds["time"] = pd.to_datetime(ds["time"])


fig = px.scatter_geo(
    ds,
    lat="latitude",
    lon="longitude",
    color="mag",
    size="mag",
    size_max=30,
    opacity=0.65,
    hover_name="place",
    animation_frame=ds["time"].dt.strftime("%Y-%m-%d %H:%M:%S"),
    projection="natural earth",
    color_continuous_scale="Turbo",
    range_color=[ds["mag"].min(), ds["mag"].max()],
)

fig.update_geos(showcountries=False, showland=True, landcolor="rgb(223, 242, 255)")
fig.update_layout(
    title="Earthquakes visualization; the week of the Kamchatka earthquake - July 25th to Augest 1st<br>"
    "Data by USGS<br>"
    "Animation by Brahim HADJ SAID",
    title_font=dict(size=18),
    title_x=0,
    mapbox_style="stamen-terrain",
    height=700,
    margin={"r": 0, "t": 90, "l": 60, "b": 0},
    coloraxis_colorbar=dict(title="Magnitude"),
)
fig.show()
