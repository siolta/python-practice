import plotly.express as px

from die import Die

# Create a D6
die_1 = Die()
die_2 = Die()

# make some rolls
results = [die_1.roll() + die_2.roll() for res in range(1000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(val) for val in poss_results]

# Visualize the results.
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize the chart.
fig.update_layout(xaxis_dtick=1)

fig.show()
