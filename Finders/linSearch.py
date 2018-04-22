length = 10
y = []
for i in range(length):
    y.append(i + 1)
    # print(y[i])

def linSearch(x):
    ans = 0
    for i in range(length):
        if y[i] == x:
            print(i, ' Yeeeahh!')
            ans = 1
    if ans == 0:
        print('Nooo...')

linSearch(10)