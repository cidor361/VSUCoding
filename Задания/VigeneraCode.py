import string

Shift = list(input('Please, enter key: '))
Alphabet = list(string.printable)
Message = list(input('Please, input message: '))
i = 0
j = 0
CurrentLetterAddIndex = 0
CurrentLetterIndex = 0
NewLetterIndex = 0
while i < len(Message):
    if j >= len(Shift):
        j -= len(Shift)
    CurrentLetterAddIndex = Alphabet.index(Shift[j])
    CurrentLetterIndex = Alphabet.index(Message[i])
    NewLetterIndex = CurrentLetterAddIndex + CurrentLetterIndex
    if NewLetterIndex > len(Alphabet):
        NewLetterIndex -= len(Alphabet)
    Message[i] = Alphabet[NewLetterIndex]
    i += 1
    j += 1
print(Message)