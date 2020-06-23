import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QInputDialog,QDialog
from EnigmaGUI import *
from tkinter import filedialog
from tkinter import *
import time



class MainScript(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButtonEncryptionS.clicked.connect(self.EnrcyptionS)
        self.ui.pushButtonDecryptionS.clicked.connect(self.DecryptionS)
        self.ui.pushButtonEncryption2E.clicked.connect(self.Enrcyption2E)
        self.ui.pushButtonDecryption2D.clicked.connect(self.Decryption2D)
        self.ui.pushButtonEncryptionER.clicked.connect(self.EnrcyptionER)
        self.ui.pushButtonDecryptionRD.clicked.connect(self.DecryptionRD)
        self.ui.pushButtonEncryption2ER.clicked.connect(self.Enrcyption2ER)
        self.ui.pushButtonDecryption2RD.clicked.connect(self.Decryption2RD)
        self.show()


    def EnrcyptionS(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Text File", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        
        clef_i = 0
        chiff = ""
        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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
        self.ui.labelStatus.setText("Status: Encryption Done!")
        fichier = open(filename, 'w')
        fichier.write(chiff)
        fichier.close()
    
    
    
    
    
    def DecryptionS(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Text File", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        clef_i = 0
        chiff = ""
        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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
        self.ui.labelStatus.setText("Decryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(chiff)
        fichier.close()
         
    
    
    
    
    
    def Enrcyption2E(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        clef_i = 0
        chiff = ""
        FinalChiff=''
        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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

        for i in chiff:
            if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
                c_ord = ord(i) + ord(clef[clef_i]) - 97
                if i <= 'Z' and c_ord > ord('Z'):
                    c_ord = 64 + c_ord - ord('Z')
                elif 'a' <= i <= 'z' and c_ord > ord('z'):
                    c_ord = 96 + c_ord - ord('z')
                c_char = chr(c_ord) 
                FinalChiff += c_char
            else:
                FinalChiff += i

            clef_i += 1
            if clef_i == len(clef):
                clef_i = 0
        self.ui.labelStatus.setText("Status: Double Encryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(FinalChiff)
        fichier.close()
        
    
    
    
    
    
    
    
    
    
    def Decryption2D(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        clef_i = 0
        chiff = ""
        FinalChiff=""

        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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
        self.ui.labelStatus.setText("Double Decryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(FinalChiff)
        fichier.close()
        
    
    
    
    
    
    
    
    
    
    def Enrcyption2E(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        clef_i = 0
        chiff = ""
        FinalChiff=''
        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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

        for i in chiff:
            if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
                c_ord = ord(i) + ord(clef[clef_i]) - 97
                if i <= 'Z' and c_ord > ord('Z'):
                    c_ord = 64 + c_ord - ord('Z')
                elif 'a' <= i <= 'z' and c_ord > ord('z'):
                    c_ord = 96 + c_ord - ord('z')
                c_char = chr(c_ord) 
                FinalChiff += c_char
            else:
                FinalChiff += i

            clef_i += 1
            if clef_i == len(clef):
                clef_i = 0
        self.ui.labelStatus.setText("Status: Double Encryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(FinalChiff)
        fichier.close()
        
    
    
    
    
    
    
    
    
    
    def Decryption2D(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        clef_i = 0
        chiff = ""
        FinalChiff=""

        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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
        self.ui.labelStatus.setText("Double Decryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(FinalChiff)
        fichier.close()
        
    
    
    
    
    
    
    
    
    
    def EnrcyptionER(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        clef_i = 0
        chiff = ""
        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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
        self.ui.labelStatus.setText("Status: Reverse Encryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(FinalChiff)
        fichier.close()
        
     
    
    
    
    def DecryptionRD(self):
        fenetre = Tk()
        filename = filedialog.askopenfilename(filetypes=[("Fichiers texte", ".txt")])
        fenetre.destroy()

        fichier = open(filename, 'r')
        chaine = fichier.read()
        fichier.close()

        
        clef_i = 0
        chiff = ""
        password,ok=QInputDialog.getText(self, "Enter your password", 
        "Enter you password")
        if ok and (len(password) !=0):
            clef = password
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


        self.ui.labelStatus.setText("Reversed Decryption Done! ")
        fichier = open(filename, 'w')
        fichier.write(chiff)
        fichier.close()
        



    def Enrcyption2ER(self):
        pass
    def Decryption2RD(self):
        pass


if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MainScript()
    w.show()
    sys.exit(app.exec_())