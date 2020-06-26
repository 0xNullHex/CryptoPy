import sys
from PyQt5.QtWidgets import QFileDialog,QWidget,QApplication,QPushButton,QLabel,QInputDialog,QDialog
from EnigmaGUI import *
import vigenere

class MainScript(QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButtonEncryptionS.clicked.connect(self.encryption)
        self.ui.pushButtonDecryptionS.clicked.connect(self.decryption)
        self.ui.pushButtonEncryption2E.clicked.connect(self.double_enrcyption)
        self.ui.pushButtonDecryption2D.clicked.connect(self.double_decryption)
        self.ui.pushButtonEncryptionER.clicked.connect(self.encryption_rev)
        self.ui.pushButtonDecryptionRD.clicked.connect(self.decryption_rev)
        self.ui.pushButtonDecryptionDER.clicked.connect(self.double_enrcyption_rev)
        self.ui.pushButtonDecryptionDRD.clicked.connect(self.double_decryption_rev)
        self.show()

    def encryption(self): self.crypt(1,1)
    
    def decryption(self): self.crypt(2,1)

    def double_enrcyption(self): self.crypt(1,2)

    def double_decryption(self): self.crypt(2,2)

    def encryption_rev(self): self.crypt(1,3)

    def decryption_rev(self): self.crypt(2,3)

    def double_enrcyption_rev(self): self.crypt(1,4)

    def double_decryption_rev(self): self.crypt(2,4)

    def askfileandread(self):
        # File chosing dialog
        filename = QFileDialog.getOpenFileName(self, caption='Open the desired file', filter='*.txt')[0]
        if len(filename) == 0:
            self.ui.labelStatus.setText("No file chosen!")
            return False
        file = open(filename, 'r')
        sequence = file.read()
        file.close()
        return sequence

    def crypt(self,choice,a):
        word = "encryption" if choice == 1 else "decryption" # Choice 1 is encryption, Choice 2 is decryption
        sequence = self.askfileandread()
        if sequence == False:
            return

        result = ""
        password,ok = QInputDialog.getText(self, "Enter your password", "Enter you password")
        if not ok or len(password) == 0:
            return

        if a == 1:
            if choice == 1:
                result = vigenere.encrypt(sequence,password) # Simple encryption
            else: 
                result = vigenere.decrypt(sequence,password) # Simple decryption
        elif a == 2:
            if choice == 1:
                result = vigenere.encrypt(vigenere.encrypt(sequence,password),password) # Double encryption
            else:
                result = vigenere.decrypt(vigenere.decrypt(sequence,password),password) # Double decryption
        elif a == 3:
            if choice == 1:
                result = vigenere.reverse(vigenere.encrypt(sequence,password)) # Simple encryption + reverse
            else:
                result = vigenere.decrypt(vigenere.reverse(sequence),password) # Reverse + simple decryption
        elif a == 4:
            if choice == 1:
                result = vigenere.reverse(vigenere.encrypt(vigenere.encrypt(sequence,password),password)) # Double encryption + reverse
            else:
                result = vigenere.decrypt(vigenere.decrypt(vigenere.reverse(sequence),password),password) # Reverse + double decryption
        
        # File chosing dialog
        file = QFileDialog.getSaveFileName(self,"Save the " + word[:-3] + "ed File",filter='*.txt')[0]
        if file:
            file = open(file + ".txt",'w')
            file.write(result) # Writing into chosen directory
            file.close()
            self.ui.labelStatus.setText((word + " done ! ").title())
        else:
            self.ui.labelStatus.setText("Cancelled. File not saved !")
            
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=MainScript()
    w.show()
    sys.exit(app.exec_())