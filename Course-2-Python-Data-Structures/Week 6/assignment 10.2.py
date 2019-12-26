#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for word in handle:
    word = word.rstrip()
    if not word.startswith('From '): continue
    lines = word.split()[5]
    pos = lines.find(':')
    hour =  lines[:pos]
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] += 1

lst = list()
for key,value in list(counts.items()):
    lst.append((key, value))

lst.sort()

for key, value in lst:
    print(key, value)