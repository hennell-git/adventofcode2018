datafile = open("data.txt")

data = [line for line in datafile]

def off_by_one(string1, string2):
    match_count = 0
    string_length = min(len(string1), len(string2))
    for i in range(0,string_length):
        if string1[i] == string2[i]:
            match_count += 1
    return match_count == (string_length -1)


def match_in_list(string1, list_of_strings):
    for word in list_of_strings:
        if off_by_one(string1,word):
            print (string1,word)

for i in range(0,len(data)):
    match_in_list(data[i],data[i+1:])
