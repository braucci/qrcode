#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
import pyqrcode
from pyqrcode import QRCode
import sys

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('qrcode.ui', self)
        self.setFixedSize(500, 390)
    

    def pB_valutaClick(self):

        try:
            # String which represents the QR code
            s = (self.lE_testo.text())
            # output file name
            filename = "qrcode.png"
            filename_svg = "qrcode.svg"
            # Generate QR Code
            img = pyqrcode.create(s)
            img.png(filename, scale=7)
            if self.cB_svg.isChecked():
                img.svg(filename_svg, scale=8)
            
            pixmap = QPixmap(filename)
            self.lab_output.setPixmap(pixmap)
            
        except:
            print('Valore nel campo non accettato')
            #self.lE_imponibile.setText('')
            #self.lE_iva.setText('')
            #self.lE_aliquota.setText('22')

    def clear_figure(self):
        self.lab_output.clear()


app = QApplication(sys.argv)
window = Ui()
window.show()
sys.exit(app.exec())