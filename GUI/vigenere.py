def encrypt(sequence,key):
    key_i = 0
    result = ""

    for i in sequence:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            c_ord = ord(i) + ord(key[key_i]) - 97
            if i <= 'Z' and c_ord > ord('Z'):
                c_ord = 64 + c_ord - ord('Z')
            elif 'a' <= i <= 'z' and c_ord > ord('z'):
                c_ord = 96 + c_ord - ord('z')
            c_char = chr(c_ord) 
            result += c_char
        else:
            result += i

    key_i += 1
    if key_i == len(key):
        key_i = 0
        
    return result

def decrypt(sequence,key):
    key_i = 0
    result = ""

    for i in sequence:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            c_ord = ord(i) - (ord(key[key_i]) - 97)
            if 'A' <= i <= 'Z' and c_ord < ord('A'):
                c_ord = 91 - (ord('A') - c_ord)
            elif i >= 'a' and c_ord < ord('a'):
                c_ord = 123 - (ord('a') - c_ord)
            c_char = chr(c_ord) 
            result += c_char
        else:
            result += i

    key_i += 1
    if key_i == len(key):
        key_i = 0

    return result

def reverse(sequence):
    result = ''
    a = len(sequence)

    for x in sequence:
        if len(sequence) != 0:
            y=sequence[a-1]
            a-=1
            result+=y

    return result