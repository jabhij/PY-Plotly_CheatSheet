# Importing Plotly Module
import plotly as py
import plotly.graph_objs as go

trace = go.Scatter (
  x = [1, 2], y = [1, 2],
  fill = 'tonexty')
data = [trace]
py,iplot(data)
