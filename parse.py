"""
Parse data from an ugly CSV or Excel file, and render it in
JSON, save to a database, and visualize in graph form.
Part I: Taking data from a CSV/Excel file, and return it into a format
that is easier for Python to play with.
"""

import csv
MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	"""Parses a raw CSV file to a JSON-line object."""

	# Open CSV file
	opened_file = open(raw_file, 'rU')
    
    # Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter) #csv_data is generator object

    # Build a data structure to return parsed_data
    # Setup an empty list
	parsed_data = []

    # Skip over the first line of the file for the headers
	fields = csv_data.next() #column headers from csv, come from first row

    # Iterate over each row of the csv file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row))) 

    # Close CSV file
	opened_file.close() 

	return parsed_data #list of dictionaries

def main():
    # Call our parse function and give it the needed parameters
	new_data = parse(MY_FILE, ",")

    # Let's see what the data looks like!
	print new_data

if __name__ == "__main__":
	main()
	# code only execute when you want to run the module as a program (via the command line)
	#  and not execute when someone just wants to import the parse() function itself into another Python file.
