# Layout Designs

# Starting with Legend and it's trace

# Trace 1
trace1 = go.Scatter(
  name = 'abhishek'
  x = [1, 2], y = [1, 2])
  
# Trace 2
trace2 = go.Scatter(
  name = 'jaiswal'
  x = [1, 2], y = [1, 2])

  
# Defining Layout
layout = go.Layout(
  showlegend = True,
  legend = dict(
  x = 0.2, y = 0.5
  )      
  
# Tracing 
data = [trace1, trace2]
fi
