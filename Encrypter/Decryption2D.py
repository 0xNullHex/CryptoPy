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
FinalChiff=""


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

for i in chiff:
    if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
        c_ord = ord(i) - (ord(clef[clef_i]) - 97)
        if 'A' <= i <= 'Z' and c_ord < ord('A'):
            c_ord = 91 - (ord('A') - c_ord)
        elif i >= 'a' and c_ord < ord('a'):
            c_ord = 123 - (ord('a') - c_ord)
        c_char = chr(c_ord) 
        FinalChiff += c_char
    else:
        FinalChiff += i

    clef_i += 1
    if clef_i == len(clef):
        clef_i = 0

fichier = open(filename, 'w')
fichier.write(FinalChiff)
fichier.close()