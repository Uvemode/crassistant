import sys
import pyperclip
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel

def disable_others(self):
    for line in line_src:
        if line != self:
            line.setText("")

def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            pass
        elif QMouseEvent.button() == Qt.RightButton:
            pyperclip.copy(self.text())
            return

QLineEdit.disable_others = disable_others
QLineEdit.mousePressEvent = mousePressEvent

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Crassistant'
        self.left = 1000
        self.top = 500
        self.width = 380
        self.height = 310
        self.initUI()

    def init_src(self, widget):
        line_src.append(widget)
        widget.textEdited.connect(widget.disable_others)
        widget.returnPressed.connect(self.convert)

    def init_cnvrt(self, widget):
        line_cnvrt.append(widget)
        widget.textEdited.connect(widget.disable_others)
        widget.returnPressed.connect(self.convert)

    def initUI(self):
            global line_src
            global line_cnvrt   
            line_src = []
            line_cnvrt = []
            
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            p = self.palette()
            p.setColor(self.backgroundRole(), QColor(50,45,30))
            p.setColor(self.foregroundRole(), QColor(253,150,31))
            self.setPalette(p)
            
            # First column labels
            self.dec_label = QLabel(self)
            self.dec_label.setText("Decimal")
            self.dec_label.move(40,20)

            self.ascii_label = QLabel(self)
            self.ascii_label.setText("ASCII")
            self.ascii_label.move(170,20)

            self.unicode_label = QLabel(self)
            self.unicode_label.setText("Unicode")
            self.unicode_label.move(280,20)

            # Second column labels
            self.hex_label = QLabel(self)
            self.hex_label.setText("Hex")
            self.hex_label.move(50,80)

            self.octal_label = QLabel(self)
            self.octal_label.setText("Octal")
            self.octal_label.move(170,80)

            self.binary_label = QLabel(self)
            self.binary_label.setText("Binary")
            self.binary_label.move(280,80)

            # Decimal
            self.decimal = QLineEdit(self)
            self.init_src(self.decimal)   
            regex = QRegExp("[0-9]+")
            input_valid = QRegExpValidator(regex, self.decimal)
            self.decimal.setValidator(input_valid)
            self.decimal.move(20, 40)
            self.decimal.resize(100,30)
            
            # Ascii
            self.ascii = QLineEdit(self)
            self.init_src(self.ascii)
            self.ascii.move(140, 40)
            self.ascii.resize(100,30)

            # Unicode
            self.unicode = QLineEdit(self)
            self.init_src(self.unicode)
            self.unicode.move(260, 40)
            self.unicode.resize(100,30)

            # Hex
            self.hex = QLineEdit(self)
            self.init_src(self.hex)
            regex = QRegExp("[A-Fa-f0-9]+")
            input_valid = QRegExpValidator(regex, self.hex)
            self.hex.setValidator(input_valid)
            self.hex.move(20, 100)
            self.hex.resize(100,30)

            # Octal
            self.octal = QLineEdit(self)
            self.init_src(self.octal)
            regex = QRegExp("[0-7]+")
            input_valid = QRegExpValidator(regex, self.octal)
            self.octal.setValidator(input_valid)
            self.octal.move(140, 100)
            self.octal.resize(100,30)

            # Binary

            self.binary = QLineEdit(self)
            self.init_src(self.binary)
            regex = QRegExp("[0-1]+")
            input_valid = QRegExpValidator(regex, self.binary)
            self.binary.setValidator(input_valid)
            self.binary.move(260, 100)
            self.binary.resize(100,30)

            # First column labels
            self.dec_label_convert = QLabel(self)
            self.dec_label_convert.setText("Decimal")
            self.dec_label_convert.move(40,180)

            self.ascii_label_convert = QLabel(self)
            self.ascii_label_convert.setText("ASCII")
            self.ascii_label_convert.move(170,180)

            self.unicode_label_convert = QLabel(self)
            self.unicode_label_convert.setText("Unicode")
            self.unicode_label_convert.move(280,180)

            # Second column labels
            self.hex_label_convert = QLabel(self)
            self.hex_label_convert.setText("Hex")
            self.hex_label_convert.move(50,240)

            self.octal_label_convert = QLabel(self)
            self.octal_label_convert.setText("Octal")
            self.octal_label_convert.move(170,240)

            self.binary_label_convert = QLabel(self)
            self.binary_label_convert.setText("Binary")
            self.binary_label_convert.move(280,240)

            # Decimal
            self.decimal_convert = QLineEdit(self)
            self.init_cnvrt(self.decimal_convert)  
            regex = QRegExp("[0-9]+")
            input_valid = QRegExpValidator(regex, self.decimal_convert)
            self.decimal_convert.setValidator(input_valid)
            self.decimal_convert.move(20, 200)
            self.decimal_convert.resize(100,30)
            
            # Ascii
            self.ascii_convert = QLineEdit(self)
            self.init_cnvrt(self.ascii_convert)
            self.ascii_convert.move(140, 200)
            self.ascii_convert.resize(100,30)

            # Unicode
            self.unicode_convert = QLineEdit(self)
            self.init_cnvrt(self.unicode_convert)
            self.unicode_convert.move(260, 200)
            self.unicode_convert.resize(100,30)

            # Hex
            self.hex_convert = QLineEdit(self)
            self.init_cnvrt(self.hex_convert)
            self.hex_convert.move(20, 260)
            self.hex_convert.resize(100,30)

            # Octal
            self.octal_convert = QLineEdit(self)
            self.init_cnvrt(self.octal_convert)
            self.octal_convert.move(140, 260)
            self.octal_convert.resize(100,30)

            # Binary
            self.binary_convert = QLineEdit(self)
            self.init_cnvrt(self.binary_convert)
            self.binary_convert.move(260, 260)
            self.binary_convert.resize(100,30)

            for line1, line2 in zip(line_src, line_cnvrt):
                line1.setStyleSheet("border: 1px solid rgb(253,150,31); background-color: rgb(50,45,30); color: rgb(161,249,248);")
                line2.setStyleSheet("border: 1px solid rgb(253,150,31); background-color: rgb(50,45,30); color: rgb(161,249,248);")
                line1.setContextMenuPolicy(Qt.NoContextMenu)
                line2.setContextMenuPolicy(Qt.NoContextMenu)
                line2.setReadOnly(True)
                
            # Convert button
            self.button = QPushButton("Convert", self)
            self.button.setCursor(Qt.PointingHandCursor)
            self.button.setStyleSheet("border: 1px solid rgb(165,225,45); background-color: rgb(50,45,30); color: rgb(165,225,45); padding: 5px 10px")
            self.button.move(150, 142)

            # Convert function
            self.button.clicked.connect(self.convert)

            self.show()


    def convert(self):
        source = None
        for line in line_src:
            if line.text():
                source = line
        if source is None:
            return
        elif source == self.decimal:
            self.convert_from_decimal()
        elif source == self.ascii:
            self.convert_from_ascii()
        elif source == self.hex:
            self.convert_from_hex()
        elif source == self.octal:
            self.convert_from_octal()
        elif source == self.binary:
            self.convert_from_binary()

    def convert_from_decimal(self):
        try:
            d = int(self.decimal.text())
        except Exception:
            return
        self.decimal.setText("")
        self.decimal_convert.setText(str(d))
        if d >= 0 and d < 256:
            self.ascii_convert.setText(chr(d))
        self.hex_convert.setText(hex(d).upper()[2:])
        self.binary_convert.setText(self.convert_to_binary(d))
        self.octal_convert.setText(oct(d)[2:]) 

    def convert_from_ascii(self):
        a = self.ascii.text()
        ascii_chars = []
        for char in a:
            ln = len(str(ord(char)))
            if ln < 3:
                diff = 3 - ln 
                ascii_chars.append(("0" * diff) +  str(ord(char)))
            else:
                ascii_chars.append(str(ord(char)))
        self.decimal_convert.setText(" ".join(ascii_chars))
        self.ascii_convert.setText(self.ascii.text())
        self.hex_convert.setText(" ".join(hex(int(x))[2:] for x in ascii_chars))
        self.octal_convert.setText(" ".join(oct(int(x))[2:] for x in ascii_chars))
        self.binary_convert.setText(" ".join(format(ord(x), 'b') for x in a)) 

    def convert_from_hex(self):
        try:
            x = int(self.hex.text(), 16)
        except Exception:
            return
        self.decimal_convert.setText(str(x))
        if x >= 0 and x < 256:
            self.ascii_convert.setText(chr(x))
        self.hex_convert.setText(self.hex.text().upper())
        self.hex.setText("")
        self.octal_convert.setText(oct(x)[2:])
        self.binary_convert.setText(self.convert_to_binary(x))
        
    def convert_from_octal(self):
        try:
            o = int(self.octal.text(), 8)
        except Exception as e:
            print(e)
            return
        self.decimal_convert.setText(str(o))
        if o >= 0 and o < 256:
            self.ascii_convert.setText(chr(o))
        self.hex_convert.setText(hex(o).upper()[2:])
        self.octal_convert.setText(self.octal.text())
        self.octal.setText("")
        self.binary_convert.setText(self.convert_to_binary(o))

    def convert_from_binary(self):
        try:
            b = int(self.binary.text(), 2)
        except Exception:
            return
        self.decimal_convert.setText(str(b))
        if b >= 0 and b < 256:
            self.ascii_convert.setText(chr(b))
        self.hex_convert.setText(hex(b).upper()[2:])
        self.octal_convert.setText(oct(b)[2:])
        self.binary_convert.setText(self.binary.text())
        self.binary.setText("")

    def convert_to_binary(self, n):
        bin_list = bin(n)[2:]
        diff = (1 - ((len(bin_list) / 4) - int((len(bin_list) / 4))))
        if not diff.is_integer():
            diff = int(diff * 4)
            bin_list = "0" * diff + bin_list 
        bin_list = " ".join([bin_list[i:i+4] for i in range (0, len(bin_list), 4)])
        return bin_list

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())