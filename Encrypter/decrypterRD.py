from tkinter import filedialog
from tkinter import *

fenetre = Tk()
filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
fenetre.destroy()

fichier = open(filename, 'r')
chaine = fichier.read()
fichier.close()

clef = input("Entrez la clef de déchiffrement : ")
clef_i = 0
chiff = ""
FinalChaine=''
a=len(chaine)
for x in chaine:
                if len(chaine)!=0:
                    y=chaine[a-1]
                    a-=1
                    FinalChaine+=y



for i in FinalChaine:
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

print(chaine)
print(FinalChaine)

fichier = open(filename, 'w')
fichier.write(chiff)
fichier.close()