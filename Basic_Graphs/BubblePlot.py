# Importing Plotly Module
import plotly as py
import plotly.graph_objs as go

trace = go.Scatter(
  x = [1,2,3], y = [1,2,3],
  marker = dict(
  color = ['red','green'],
  size = [25, 50, 200]),
  mode = 'markers')
py.iplot([trace])
