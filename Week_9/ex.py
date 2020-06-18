import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(THIS_FOLDER, 'nameslist.txt')

# 1 Read the file line by line
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("Line {}: {}".format(cnt, line.strip()))
        line = fp.readline()
        cnt += 1

# 2 Read only the 5th line of the file
with open(filepath) as fp:
    for i, line in enumerate(fp):
        if i == 5:
            print("Line {}: {}".format(i, line.strip()))

# 3 Read only the 5th first characters of the file
with open(filepath) as fp:
    line = fp.readline()
    for i, line in enumerate(fp):
        print("Line {}: {}".format(i, line.strip()))
        line = fp.readline()
        i += 1
        if i > 4:
            break

# 4 Read all the file and return it as a list of strings. Then split each word
with open(filepath) as fp:
    flat_list = [word for line in fp for word in line.split()]
print(flat_list)

# 5 Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
with open(filepath) as fp:
    flat_list = [word for line in fp for word in line.split()]
    names = []
    for i in flat_list:
        if i not in names:
            names.append(i)
    for i in range(0, len(names)):
        print(names[i], 'is', flat_list.count(names[i]), 'times')

# 6 Append your first name at the end of the file
with open(filepath, 'a+') as fp:
    fp.write('\nMaria')

# 7 Append "SkyWalker" next to each first name "Luke"
