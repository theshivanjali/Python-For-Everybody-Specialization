# Handling The Data
# The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re

total = 0

fname = input("Enter file name: ")
file = open(fname)
for line in file:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    for num in nums:
        total = total + int(num)
print(total)