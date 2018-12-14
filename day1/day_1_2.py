datafile = open('data.txt')

data = [int(line) for line in datafile]
output = 0
seenvalues = {}
dupe = 0
while dupe == 0:
    for value in data:
        output += value
        if output in seenvalues:
            dupe = output
            break
        else:
            seenvalues[output] = 1


print dupe
