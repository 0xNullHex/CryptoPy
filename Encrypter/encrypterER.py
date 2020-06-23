from tkinter import filedialog
from tkinter import *

fenetre = Tk()
filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
fenetre.destroy()

fichier = open(filename, 'r')
chaine = fichier.read()
fichier.close()

clef = input("Entrez la clef de chiffrement : ")
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

FinalChiff=''
a=len(chiff)
for x in chiff:
                if len(chiff)!=0:
                    y=chiff[a-1]
                    a-=1
                    FinalChiff+=y
print(chiff)
print(FinalChiff)

fichier = open(filename, 'w')
fichier.write(FinalChiff)
fichier.close()