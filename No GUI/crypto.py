
from tkinter import filedialog
from tkinter import *
import vigenere

def askfileandread():
    fenetre = Tk()
    filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
    fenetre.destroy()
    if len(filename) == 0:
        print("No file chosen. Aborting !")
        return False
    fichier = open(filename, 'r')
    chaine = fichier.read()
    fichier.close()
    return chaine

def encrypt():
    print("\nChoose your encryption type :")
    print("1) Simple encryption\n2) Double encryption\n3) Encryption + Reverse\n4) Double encryption + Reverse\n5) Main Menu\n")
    while True:
            try:
                a = int(input(">>> "))
            except:
                print("Invalid entry ! Retry.")
                continue
            if a == 5:
                return
            if 1 <= a <= 4:
                break
            else:
                print("Invalid entry ! Retry.")
                continue
    print("\nChoose your file...")

    chaine = askfileandread()
    if chaine == False:
        return

    result = ""
    clef = input("Enter encryption key : ")
    if a == 1:
        result = vigenere.chiff(chaine,clef)
    elif a == 2:
        result = vigenere.chiff(vigenere.chiff(chaine,clef),clef)
    elif a == 3:
        result = vigenere.reverse(vigenere.chiff(chaine,clef))
    elif a == 4:
        result = vigenere.reverse(vigenere.chiff(vigenere.chiff(chaine,clef),clef))
    
    output = "enc.txt"
    fichier = open(output, 'w')
    fichier.write(result)
    fichier.close()
    print("Encrypted file saved in " + output)

def decrypt():
    print("\nChoose your decryption type :")
    print("1) Simple decryption\n2) Double decryption\n3) Decryption + Reverse\n4) Double decryption + Reverse\n5) Main Menu\n")
    a = int(input(">>> "))
    print("\nChoose your file...")

    chaine = askfileandread()
    if chaine == False:
        return

    result = ""
    clef = input("Enter decryption key : ")
    if a == 1:
        result = vigenere.dechiff(chaine,clef)
    elif a == 2:
        result = vigenere.dechiff(vigenere.dechiff(chaine,clef),clef)
    elif a == 3:
        result = vigenere.dechiff(vigenere.reverse(chaine),clef)
    elif a == 4:
        result = vigenere.dechiff(vigenere.dechiff(vigenere.reverse(chaine),clef),clef)
    
    output = "dec.txt"
    fichier = open(output, 'w')
    fichier.write(result)
    fichier.close()
    print("Decrypted file saved in " + output)

def main():
    print(" Welcome to Enigma (for .txt files) ".center(80,'*'))
    while (True):
        print("\nWhat do you want ?\n1) Encrypt\n2) Decrypt\n3) Exit")
        c = int(input("\n>>> "))
        if c == 1:
            encrypt()
        elif c == 2:
            decrypt()
        elif c == 3:
            break
        else:
            print("Invalid entry ! Retry.")

if __name__ == "__main__":
    main()