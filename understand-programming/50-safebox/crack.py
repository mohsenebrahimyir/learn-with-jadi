def sit(a, b):
    correct = 0
    found = 0
    ar = []
    br = []
    for i in range(len(a)):
        if a[i] == b[i]:
            correct += 1
        else:
            ar.append(a[i])
            br.append(b[i])

    for c in ar:
        if c in br:
            found += 1
            br.remove(c)

    return correct, found


for i in range(0, 1000):
    i = str(i).zfill(3)
    if sit(i, "682") == (1, 0) and \
       sit(i, "614") == (0, 1) and \
       sit(i, "206") == (0, 2) and \
       sit(i, "738") == (0, 0) and \
       sit(i, "380") == (0, 1):
           print(i)