import string

while True:
    try:
        Shift = int(input('Please, enter key: '))
        if Shift > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print("Incorrect input data. Please enter again")
Alphabet = str(string.printable)
Message = str(input('Please, input message: '))
Str = ''
for i in Message:
    Str += Alphabet[(Alphabet.index(i) + Shift) % len(Alphabet)]
print(Str)