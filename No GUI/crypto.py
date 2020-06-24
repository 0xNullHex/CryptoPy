
from tkinter import filedialog
from tkinter import *
import vigenere

def askfileandread():
    fenetre = Tk()
    filename = filedialog.askopenfilename(filetypes=[("Text files", ".txt")])
    fenetre.destroy()
    if len(filename) == 0:
        print("No file chosen. Aborting !")
        return False
    file = open(filename, 'r')
    chaine = file.read()
    file.close()
    return chaine

def crypt(choice):
    if choice == 1:
        word = "encryption"
        output = "enc.txt"
    else:
        word = "decryption"
        output = "dec.txt"
    print("\nChoose your " + word + " type :")
    print(("1) Simple " + word + "\n2) Double " + word + "\n3) " + word + " + Reverse\n4) Double " + word + " + Reverse\n5) Main Menu\n").title())
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
    clef = input("Enter " + word + " key : ")

    if a == 1:
        if choice == 1:
            result = vigenere.encrypt(chaine,clef)
        else: 
            result = vigenere.decrypt(chaine,clef)
    elif a == 2:
        if choice == 1:
            result = vigenere.encrypt(vigenere.encrypt(chaine,clef),clef)
        else:
            result = vigenere.decrypt(vigenere.decrypt(chaine,clef),clef)
    elif a == 3:
        if choice == 1:
            result = vigenere.reverse(vigenere.encrypt(chaine,clef))
        else:
            result = vigenere.decrypt(vigenere.reverse(chaine),clef)
    elif a == 4:
        if choice == 1:
            result = vigenere.reverse(vigenere.encrypt(vigenere.encrypt(chaine,clef),clef))
        else:
            result = vigenere.decrypt(vigenere.decrypt(vigenere.reverse(chaine),clef),clef)

    file = open(output, 'w')
    file.write(result)
    file.close()
    print("Encrypted file saved in " + output)

def main():
    print(" Welcome to Enigma (for .txt files) ".center(80,'*'))
    while (True):
        print("\nWhat do you want ?\n1) Encrypt\n2) Decrypt\n3) Exit")
        c = int(input("\n>>> "))
        if c == 1 or c == 2:
            crypt(c)
        elif c == 3:
            break
        else:
            print("Invalid entry ! Retry.")

if __name__ == "__main__":
    main()