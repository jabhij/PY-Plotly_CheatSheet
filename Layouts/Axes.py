# Layouts -- Axis Information

# Base trace data
trace = go.Scatter(
  x = [1, 2, 3, 4]
  y = [1, 2, 3, 6])
  
axis_template = dict(
  showgrid = False
  zeroline = False
  nticks = 15
  showline = True
  title = 'Legend -- Axis Demo'
  mirror = 'all')
 
# Plotting 
data = [trace]
fig = go.figure(
  data = data,
  layout = layout)
py.iplot(fig)
  
