# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# import string

# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for word in handle:
    word = word.rstrip()
    if not word.startswith('From '): continue
    lines = word.split()
    if lines[1] not in counts:
        counts[lines[1]] = 1
    else:
        counts[lines[1]] += 1

largest = None
for key in counts:
    if largest is None or counts[key] > largest :
        largest = counts[key]
        largeKey = key
print(largeKey, largest)