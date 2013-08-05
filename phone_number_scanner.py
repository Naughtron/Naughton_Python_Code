# import regular expressions 
import re
# import argv 
from sys import argv

#arguments to provide at command line 
script, filename = argv

#load the file
data = open(filename)
#read the file
read_file = data.read()

# create a regular expression to filter out phone numbers 
phone_finder = re.compile(r"\(\d{3}\)\s*\d{3}-\d{4}")

# r to tell its a raw string
# \( to match "("
# \d{3} to match 3 digits
# \) to match ")"
# \s* account for no spaces
# \d{3} to match 3 digits
# - to match an "-"
# \d{4} to match 4 digits

# print the results
print phone_finder.findall(read_file)

