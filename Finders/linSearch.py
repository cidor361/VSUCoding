def linSearch(Array, x):
    Answer = 0
    i = 0
    for i in range(len(Array)):
        if Array[i] == x:
            Answer = i
    return Answer