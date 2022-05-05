DIRS = ['hapax_whole','hapax_ksiazki','hapax_nieksiazki']

line_count = 0
for dir in DIRS:
    file = open(dir + '.txt')
    for line in file:
        if line != "\n":
            line_count += 1


