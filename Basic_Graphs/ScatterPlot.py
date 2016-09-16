# Importing Plotly Module
import plotly as py
import plotly.graph_objs as go

trace = go.Scatter(
  x = [1, 2, 3], y = [1, 2, 3],
  text = ['A', 'B', 'C'],
  textposition = 'top center',
  mode = 'markers+text')
mode = [trace]
py.iplot (data)
