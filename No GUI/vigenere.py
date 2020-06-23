def chiff(chaine,clef):
    clef_i = 0
    chiff = ""

    for i in chaine:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            c_ord = ord(i) + ord(clef[clef_i]) - 97
            if i <= 'Z' and c_ord > ord('Z'):
                c_ord = 64 + c_ord - ord('Z')
            elif 'a' <= i <= 'z' and c_ord > ord('z'):
                c_ord = 96 + c_ord - ord('z')
            c_char = chr(c_ord) 
            chiff += c_char
        else:
            chiff += i

    clef_i += 1
    if clef_i == len(clef):
        clef_i = 0
        
    return chiff

def dechiff(chaine,clef):
    clef_i = 0
    chiff = ""

    for i in chaine:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            c_ord = ord(i) - (ord(clef[clef_i]) - 97)
            if 'A' <= i <= 'Z' and c_ord < ord('A'):
                c_ord = 91 - (ord('A') - c_ord)
            elif i >= 'a' and c_ord < ord('a'):
                c_ord = 123 - (ord('a') - c_ord)
            c_char = chr(c_ord) 
            chiff += c_char
        else:
            chiff += i

    clef_i += 1
    if clef_i == len(clef):
        clef_i = 0

    return chiff

def reverse(chaine):
    result = ''
    a = len(chaine)

    for x in chaine:
        if len(chaine) != 0:
            y=chaine[a-1]
            a-=1
            result+=y

    return result