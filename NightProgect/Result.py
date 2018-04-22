addresArray = []
numOfBites = []
numOfSessions = []
min = []
hours = []
days = []
session = 1
# session = int(input('Введите длительность сессии:'))

f = open('edu.ssl.access.log.1')
# f = open('T')                                                                              #reading each str of file
for line in f:

    i = 0
    addres = ''
    currDay = 0
    currHours = 0
    CurrMin = 0
    currByte = ''
    currIntByte = 0

    while line[i] != ' ':                                                                  #reading current mins, hours, days,addresses, num of bytes
        addres += line[i]
        i += 1

    i += 6

    currDay = int(line[i])*10+int(line[i+1])

    while line[i] != ':':
        i += 1
    i += 1
    currHours = int(line[i])*10 + int(line[i + 1])

    i += 3

    currMin = int(line[i])*10 + int(line[i + 1])

    while line[i] != "]":
        i += 1

    while line[i] != '"':
        i += 1

    i += 1

    if line[i] == 'G':
        i += 4
    elif line[i] == 'P':
        i += 5

    while line[i] != ' ':
        i += 1

    i += 1

    while line[i] != '"':
        i += 1

    i += 2

    while line[i] != ' ':
        i += 1

    i += 1

    while line[i] != ' ':
        currByte += line[i]
        i += 1
    currIntByte = int(currByte)

    lakmus = 0                                                                               #Definite and create array of vals of date, time, addresses
    j = 0
    for j in range(len(addresArray)):
        if addresArray[j] == addres:                                                         #Finding similar addresses
            lakmus = j

    if lakmus != 0:
        numOfBites[lakmus] += currIntByte
        if (currMin - min[lakmus] >= session) or (currHours > hours[lakmus]) or (currDay > days[lakmus]):
            numOfSessions[lakmus] += 1
            days[lakmus] = currDay
            hours[lakmus] = currHours
            min[lakmus] = currMin


    else:                                                                                     #Creating arrays of vals
        addresArray.append(addres)
        numOfBites.append(currIntByte)
        numOfSessions.append(1)
        days.append(currDay)
        hours.append(currHours)
        min.append(currMin)

print(addresArray)
print(numOfBites)
print(numOfSessions)
print(days)
print(hours)
print(min)

head = "<head><meta charset=\"UTF-8\"><title>Statistic</title></head>"                           #Creating HTML table
body_begin = "<body>"
body_end = "</body>"

html = "<!DOCTYPE html>\n<html lang=\"en\">" + head + body_begin
html += "<h1>Statistic</h1><ul>"
html += '<table>'
for i in range(len(addresArray)):
    html += '<tr>'
    html += '<td>'
    html += addresArray[i]
    html += '</td>'
    html += '<td>'
    html += str(numOfBites[i])
    html += '</td>'
    html += '<td>'
    html += str(numOfSessions[i])
    html += '</td>'
    # html += '<td>'
    # html +=
    # html += '</td>'
    # html += '</tr>\n'
html += '</table>'

html += "</ul>" + body_end + "</html>"

index_file = open("index.html", "w")
index_file.write(html)
index_file.close()