import urllib.request

FirstNames = []
SecondNames = []
Links = []
Lines = []
CurrURLEnding = 0
CurrFirstNameEnding = 0
CurrSecondNameEnding = 0
www = 'https://ru.wikipedia.org'
Length = 0


def BubbleSort(A, B, C):
    for j in range(len(A) - 1, 0, -1):
        for i in range(0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                B[i], B[i + 1] = B[i + 1], B[i]
                C[i], C[i + 1] = C[i + 1], C[i]

link = urllib.request.urlopen('https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D0%B8_%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F')
for line in link.readlines():
    if line.find(b'<li>') != -1 and line.find(b'a href') != -1:
        Lines.append(line)

for i in range(len(Lines)):
    Lines[i] = Lines[i].decode('utf-8')

for i in range(len(Lines)):
    Lines[i] = Lines[i].replace('\t\t\t<li>', '')
    Lines[i] = Lines[i].replace('\"', '')
    Lines[i] = Lines[i].replace('<a href=', '')
    Lines[i] = Lines[i].replace('target=_blank>', '')
    Lines[i] = Lines[i].replace('</a></li>', '')
    Lines[i] = Lines[i].replace('</ul>', '')
    Lines[i] = Lines[i].replace("\r\n", '')
    Lines[i] = Lines[i].replace('<ul>', '')
    Lines[i] = Lines[i].replace("<li>", '')
    Lines[i] = Lines[i].replace('\n', '')
    Lines[i] = Lines[i].replace('title=', '')
    Lines[i] = Lines[i].replace(',', '')
    Lines[i] = Lines[i].replace('>', '')
    Lines[i] = Lines[i].replace('</div<div', '')
    Lines[i] = Lines[i].replace('class=mw-category-group<h3', '')
    Lines[i] = Lines[i].replace('</div<div', '')
    Lines[i] = Lines[i].replace('</h', '')
    Lines[i] = Lines[i].replace('</div</div</di', '')

for i in range(len(Lines) - 1):
    line = Lines[i]
    j = 0
    CurrURLEnding = 0
    CurrFirstNameEnding = 0
    CurrSecondNameEnding = 0

    while line[j] != ' ':
        j += 1
    Links.append(line[0:j])
    j += 1
    CurrURLEnding = j

    while line[j] != ' ':
        j +=1
    FirstNames.append(line[CurrURLEnding:j])
    j += 1

    while line[j] != ' ':
        j += 1
    j += 1
    CurrFirstNameEnding = j

    while (j != len(line) - 1) and (line[j] != ' '):
        j += 1
    SecondNames.append(line[CurrFirstNameEnding:j])



Sort = input('If you want sort by first or second name enter "F" or "S": ')
print('\n')
if Sort == 'F':
    BubbleSort(FirstNames, SecondNames, Links)
    for i in range(len(Links)):
        print(FirstNames[i], SecondNames[i], www+Links[i])
elif Sort =='S':
    BubbleSort(SecondNames, FirstNames, Links)
    for i in range(len(Links)):
        print(SecondNames[i], FirstNames[i], Links[i])