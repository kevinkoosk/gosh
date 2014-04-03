import sys
import csv
import os
 
if len(sys.argv) < 1:
	print "Usage: python column2.py client_record.csv"
        print "Client record must be in CSV format"
	exit(1)

# Open the client record CSV file for reading
cr = csv.reader(open(sys.argv[1]))
cr.next()

# Input = 1234.csv, Client ref = 1234.
client = sys.argv[1].split('.')[0]

# Open target file for writing (appending)
targetfile = open("../out/middle.html","a")

# Append row and first cell, Record number
targetfile.write('<tr><td><div title="View transactions"><a href=out/' + client + '.html>' + client + '</a></div></td>')


# Open the client's personal details record (1234.txt - first line)
with open(client + '.haml', 'r') as f:  
  clientname = f.readline().split('~')[1]

# Create 1234profile.html in out/ by calling hamlpy on the haml file.
os.system('sudo hamlpy ' + client + '.haml ../out/' + client + 'profile.html')

# Append second cell, Client's name
targetfile.write('<td><div title="View file record"><a href=out/' + client + 'profile.html>' + clientname + '</a></div></td>')


# Calculate column[2] amount
amtstr = str(sum(int(x[2]) for x in cr))

# Append values (client ref.) and (amount)
targetfile.write('<td>' + amtstr + '</td></tr>')

exit(0)