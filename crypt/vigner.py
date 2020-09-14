alf = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            mj = alf.index(ch)
            kj = alf.index(key[(index - space) % len(key)])
            cj = (mj + kj) % len(alf)
            result.append(alf[cj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)

def decrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            cj = alf.index(ch)
            kj = alf.index(key[(index - space) % len(key)])
            mj = (cj - kj) % len(alf)
            result.append(alf[mj])
        else:
            space += 1
            result.append(' ')
    return ''.join(result)

