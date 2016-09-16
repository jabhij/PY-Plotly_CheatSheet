# Importing Plotly Module
import plotly as py
import plotly.graph_objs as go

trace = go.Bar(
  x = [1, 2], y = [1, 2])
data = [trace]
py.iplot(data)  
