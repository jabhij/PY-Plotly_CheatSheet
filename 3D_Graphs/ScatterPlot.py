trace = go.Scatter3D(
  x = [9, 8, 5, 1], 
  y = [1, 2, 4, 8],
  z = [11, 8, 15, 3],
  mode = 'markers')
  
# Tracing
data = [trace]
py.iplot(data)
