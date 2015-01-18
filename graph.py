"""
Take the parsed data from parse.py and visualize it using popular
Python math libraries
"""

# ordering imports
# Standard Library modules
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
# External/third party packages/modules

# Internal/self-written modules
import parse

MY_FILE = "sample_sfpd_incident_all.csv"

def visualize_days():
	"""Visualize data by day of week"""
	# grab our parsed data that we parsed earlier
	data_file = parse.parse(MY_FILE, ",")

    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
	counter = Counter(item["DayOfWeek"] for item in data_file)

	""" 
	# if don't want to use Collections counter, code below does the same thing 
	counter_alt = {}
	for item in data_file:
		if item["DayOfWeek"] in counter_alt:
			counter_alt[item["DayOfWeek"]] += 1
		else:
			counter_alt[item["DayOfWeek"]] = 1
	print counter_alt
	"""

    # Separate out the counter to order it correctly when plotting the y-axis.
	data_list = [
			counter["Monday"],
			counter["Tuesday"],
			counter["Wednesday"],
			counter["Thursday"],
			counter["Friday"],
			counter["Saturday"],
			counter["Sunday"]
				] #manually write out each counter key to force the order we want
	day_tuple = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")
    
    # Assign the data to a plot
	plt.plot(data_list)
    
    # Assign labels to the plot
	plt.xticks(range(len(day_tuple)), day_tuple) #1st parameter sets the locations, 2nd labels of the xticks

    # save the plot!
	plt.savefig("Days.png")

    # close plot file
	plt.clf()

def visualize_type():
	"""Visualize data by category in a bar graph"""
	data_file = parse.parse(MY_FILE, ",")

	#returns a dict where it sums the total incidents per Category.
	counter = Counter(item["Category"] for item in data_file)

	# Set the labels which are based on the keys of our counter.
	# Since order doesn't matter, we can just used counter.keys()
	labels = tuple(counter.keys())

	# Set where the labels hit the x-axis
	xlocations = np.arange(len(labels)) + 0.5 # using np because range doesn't work with floats and even if we
	                                          # force it to work it will involve additional divisions

	# Width of each bar
	width = 0.5

	# Assign data to a bar plot
	plt.bar(xlocations, counter.values(), width=width)

	# Assign labels and tick location to x-axis
	plt.xticks(xlocations + width / 2, labels, rotation=90) #1st param will place the center of the bar in the middle of the xtick

	# Give some more room so the labels aren't cut off in the graph
	plt.subplots_adjust(bottom=0.4) # subplots allow rendering multiple graphs on one window/function
									# With one graph, subplots can be used to adjust the spacing around the graph itself
	
	# Make the overall graph/figure larger
	plt.rcParams['figure.figsize'] = 12, 8

	# Save the plot!
	plt.savefig("Type.png")

	# Close figure
	plt.clf()

def main():
	#visualize_days()
	visualize_type()

if __name__ == "__main__":
	main()