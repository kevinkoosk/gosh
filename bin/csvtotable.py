#!/usr/bin/python
# create html table from csv
# Author(s): Chris Trombley <ctroms@gmail.com>
# Version 2 - added css class to all columns except header

#!/usr/bin/python
# create html table from csv

import sys
import csv
 
# Open the CSV file for reading
reader = csv.reader(open(sys.argv[1]))

# Create the HTML file for output
htmlfile = open(sys.argv[1] + ".output","w")

# initialize rownum variable
rownum = 0

# generate table contents
for row in reader: # Read a single row from the CSV file

	# write header row. assumes first row in csv contains header
	if rownum == 0: # do nothing for headers
           print ''

  	#write all other rows	
  	else:
  		htmlfile.write('<tr>')	# write <tr> tag
  		for column in row:
  			htmlfile.write('<td>' + column + '</td>\n')
  		htmlfile.write('</tr>')	# close </tr> tag
	
	#increment row count	
	rownum += 1

# print results to shell
exit(0)