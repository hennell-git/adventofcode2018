datafile = open('data.txt')

output = 0
for value in datafile:
    output += int(value)

print output
