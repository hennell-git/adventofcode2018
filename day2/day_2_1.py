datafile = open("data.txt")

def lettercount(box):
    letters = {}
    for letter in box:
        if letter in letters:
            letters[letter] += 1
        else: letters[letter]=1

    return letters


def hascount(count_value, count_dict):
    return count_value in count_dict.values()


two_count = 0
three_count = 0
for line in datafile:
    letters = lettercount(line)
    if hascount(2,letters): two_count += 1
    if hascount(3,letters): three_count += 1
print (two_count * three_count)

