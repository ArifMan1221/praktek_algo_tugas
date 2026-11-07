import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class LoginApp(QMainWindow):

  def __init__(self):
    super().__init__()
    loadUi(str(Path(__file__).with_name("login.ui")), self)

    self.btnlogin.clicked.connect(self.handle_login)
    self.btnclear.clicked.connect(self.clear_form)

    self.lineEdit.setFocus()
    self.lineEdit_2.setEchoMode(self.lineEdit_2.EchoMode.Password)

  def handle_login(self):
    username = self.lineEdit.text().strip()
    password = self.lineEdit_2.text()

    if username == "admin" and password == "123":
      QMessageBox.information(self, "Login Sukses", "Selamat datang Admin!")
      self.label_3.setText("✓ Login berhasil!")
      self.label_3.setStyleSheet("color: green; font-weight: bold;")
    else:
      QMessageBox.warning(
          self, "Login Gagal", "Username atau password salah!"
      )
      self.label_3.setText("✗ Username atau password salah!")
      self.label_3.setStyleSheet("color: red; font-weight: bold;")
      self.lineEdit_2.clear()
      self.lineEdit_2.setFocus()

  def clear_form(self):
    self.lineEdit.clear()
    self.lineEdit_2.clear()
    self.label_3.clear()
    self.lineEdit.setFocus()


if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = LoginApp()
  window.show()
  sys.exit(app.exec_())
  