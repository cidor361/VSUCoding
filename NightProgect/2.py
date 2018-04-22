addressesArray = []
numOfSessions = []
time = []
numOfBites = []

addressesArray.append('0.0.0.0')
numOfBites.append(0)
time.append(0)
numOfSessions.append(0)

f = open('T')
for line in f:

    i = 0
    CurrAddress = ''
    Currdate = ''
    CurrRequest = ''
    CurrHours = ''
    CurrTypeOfRequest = ''
    CurrVersionOfHTTP = ''
    CurrStatusCode = ''
    CurrNumOfBytes = ''

    while line[i] != ' ':
        CurrAddress += line[i]
        i += 1

    while line[i] != "[":
        i += 1

    while line[i] != ' ':
        i += 1
        Currdate += line[i]

    i += 1

    while line[i] != "]":
        CurrHours += line[i]
        i += 1

    while line[i] != '"':
        i += 1

    i += 1

    if line[i] == 'G':
        CurrTypeOfRequest = 'GET'
        i += 4
    elif line[i] == 'P':
        CurrTypeOfRequest = 'POST'
        i += 5

    while line[i] != ' ':
        CurrRequest += line[i]
        i += 1

    i += 1

    while line[i] != '"':
        CurrVersionOfHTTP += line[i]
        i += 1

    i += 2

    while line[i] != ' ':
        CurrStatusCode += line[i]
        i += 1

    i += 1

    while line[i] != ' ':
        CurrNumOfBytes += line[i]
        i += 1
    CurrNumOfBytes = int(CurrNumOfBytes)

    # print(address)
    # print(date)
    # print(hours)
    # print(typeOfRequest)
    # print(request)
    # print(versionOfHTTP)
    # print(statusCode)
    # print(currNumOfBytes)
    # print()














    lakmus = 0
    j = 1
    for j in range(len(addressesArray)):
        if addressesArray[j] == CurrAddress:
            lakmus = j

    if lakmus != 0:
        numOfBites[lakmus] += CurrNumOfBytes

    else:
        addressesArray.append(CurrAddress)
        numOfBites.append(CurrNumOfBytes)

print(addressesArray)
print(numOfBites)