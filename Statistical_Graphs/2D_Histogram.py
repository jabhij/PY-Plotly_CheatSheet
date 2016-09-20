# Using Trace and histogram func
trace = go.Histogram2d(
  x = [2, 4, 4, 5, 6, 6, 8, 10],
  x = [2, 4, 4, 5, 6, 6, 8, 10])

# Data Access and Plot
data = [trace]
py.iplot(data)
