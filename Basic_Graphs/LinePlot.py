# Importing Plotly Module
import plotly as py
import plotly.graph_objs as go

# Traces for Line Plot
trace1 = go.scatter(
  x=[1,5], y=[1,5])
trace2 = go.scatter(
  x=[1,5], y=[5,1])
py.iplot([trace1, trace2])
