import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui.gui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self): 
        self.setFixedSize(480, 736)
        self.setWindowIcon(QIcon('img/currency-exchange_logo200.png'))
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.inputCurrency.text()
        output_currency = self.ui.outputCurrency.text()
        input_amount = int(self.ui.inputAmount.text())     
        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        self.ui.outputAmount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()
 
sys.exit(app.exec())