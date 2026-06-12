import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow


class PlayFairApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_encrypt.clicked.connect(self.encrypt)
        self.ui.btn_decrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        url = "http://127.0.0.1:5050/api/playfair/encrypt"

        try:
            payload = {
                "plain_text": self.ui.txt_plain_text.toPlainText(),
                "key": self.ui.txt_key.toPlainText()
            }

            r = requests.post(url, json=payload)

            if r.status_code == 200:
                self.ui.txt_cipher_text.setPlainText(
                    r.json()["encrypted_message"]
                )
            else:
                QMessageBox.warning(self, "Error", r.json()["error"])

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def decrypt(self):
        url = "http://127.0.0.1:5050/api/playfair/decrypt"

        try:
            payload = {
                "cipher_text": self.ui.txt_cipher_text.toPlainText(),
                "key": self.ui.txt_key.toPlainText()
            }

            r = requests.post(url, json=payload)

            if r.status_code == 200:
                self.ui.txt_plain_text.setPlainText(
                    r.json()["decrypted_message"]
                )
            else:
                QMessageBox.warning(self, "Error", r.json()["error"])

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayFairApp()
    window.show()
    sys.exit(app.exec_())