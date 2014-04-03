# GO.sh
Simple accounting system using CSV and HAML to generate HTML.

## Requirements
This program requires 
1. [bash scripting](http://www.tldp.org/LDP/abs/html/) (Linux)
2. [Python](https://www.python.org/) and 
3. [HamlPy](https://pypi.python.org/pypi/hamlpy)

### How it works
Your records are kept in CSV and HAML. You can view them in a web browser. Run *GO.sh* on a folder containing the data and it will generate an index of records with balance. At the same time it generates HTML versions of your CSV and HAML files. HTML records are linked to the index file.

### Keeping records
Keep transaction records in CSV files. Keep notes in HAML files. If your record number is *19009*, you'd have *19009.csv* and *19009.haml* in the same place.

### Example usage
<pre>./GO.sh example</pre>
1. Runs *GO.sh* on the directory *example*.
2. Generates *table.html* and files in *out*.
3. View *table.html* to see index.
