import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator")
        self.setGeometry(300, 300, 250, 300)

        layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("font-size: 20px; padding: 5px;")
        layout.addWidget(self.display)

        # Tombol
        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row, col = 0, 0
        for btn_text in buttons:
            button = QPushButton(btn_text)
            button.setStyleSheet("font-size: 16px; padding: 10px;")
            button.clicked.connect(self.on_button_click)
            grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid)
        self.setLayout(layout)
        self.expression = ""
        self.reset_next = False  # Flag untuk mereset layar setelah menekan '='

    def on_button_click(self):
        button = self.sender()
        text = button.text()

        if text == 'C':
            self.expression = ""
            self.reset_next = False
        elif text == '=':
            try:
                # Menghitung hasil ekspresi matematika
                result = str(eval(self.expression))
                self.expression = result
            except:
                self.expression = "Error"
            self.reset_next = True  # Tandai bahwa perhitungan baru saja selesai
        else:
            # Jika layar menampilkan "Error" atau baru saja menghitung hasil (=), 
            # mulai ekspresi baru jika tombol yang ditekan adalah angka
            if self.expression == "Error" or self.reset_next:
                if text in '0123456789':
                    self.expression = text
                else:
                    # Jika operator yang ditekan setelah '=', lanjutkan dengan hasil sebelumnya
                    if self.reset_next:
                        self.reset_next = False
                    else:
                        self.expression = ""
                if self.expression != text:
                    self.expression += text
                self.reset_next = False
            else:
                self.expression += text

        self.display.setText(self.expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())