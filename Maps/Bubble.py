# Using dict elements
trace = dict(
  type = 'Scattergo'
  
  # Longitude and Latitude
  lon = [28.4355645, 26.3556464], lat = [0, 0],
  marker = dict(
      marker = ['red', 'green'],
      size = [25, 50]),

# Plot
mode = 'markers')
py.iplot([trace])
