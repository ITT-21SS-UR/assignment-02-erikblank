import sys
from PyQt5 import uic, QtCore, QtWidgets, QtGui


class Calculator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.expression = ""
        self.delete = "delete"
        self.clear = "clear"
        self.err = "Syntax Error"
        self.initUI()
        self.connectButtons()

    def initUI(self):
        self.ui = uic.loadUi("calculator.ui", self)
        self.show()

    def connectButtons(self):
        self.ui.btn_0.clicked.connect(lambda x: self.onClick('0'))
        self.ui.btn_1.clicked.connect(lambda x: self.onClick('1'))
        self.ui.btn_2.clicked.connect(lambda x: self.onClick('2'))
        self.ui.btn_3.clicked.connect(lambda x: self.onClick('3'))
        self.ui.btn_4.clicked.connect(lambda x: self.onClick('4'))
        self.ui.btn_5.clicked.connect(lambda x: self.onClick('5'))
        self.ui.btn_6.clicked.connect(lambda x: self.onClick('6'))
        self.ui.btn_7.clicked.connect(lambda x: self.onClick('7'))
        self.ui.btn_8.clicked.connect(lambda x: self.onClick('8'))
        self.ui.btn_9.clicked.connect(lambda x: self.onClick('9'))
        self.ui.btn_multiply.clicked.connect(lambda x: self.onClick('*'))
        self.ui.btn_divide.clicked.connect(lambda x: self.onClick('/'))
        self.ui.btn_plus.clicked.connect(lambda x: self.onClick('+'))
        self.ui.btn_minus.clicked.connect(lambda x: self.onClick('-'))
        self.ui.btn_equal.clicked.connect(lambda x: self.onClick('='))
        self.ui.btn_dot.clicked.connect(lambda x: self.onClick("."))
        self.ui.btn_delete.clicked.connect(lambda x: self.onClick(self.delete))
        self.ui.btn_clear.clicked.connect(lambda x: self.onClick(self.clear))

    def log_btn(message):
        def func_decorator(func):
            def logging(self, input):
                print(message + input)
                func(self, input)

                result = self.ui.text_result.text()

                if input == "=":
                    print("Result is: " + result)

                if result == self.err:
                    print("There was an " + self.err)
            return logging
        return func_decorator

    @log_btn("This Button was clicked: ")
    def onClick(self, input):
        textField = self.ui.text_result
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        operators = [".", "*", "/", "+", "-"]
        inputs = numbers + operators

        if textField.text() == self.err:
            textField.setText("")

        if input in inputs:
            textField.setText(textField.text() + input)

        if input == "=":
            try:
                result = eval(textField.text())
                textField.setText(str(result))
            except SyntaxError:
                textField.setText(self.err)
        if input == self.delete:
            textField.setText("")

        if input == self.clear:
            textField.setText(textField.text()[:-1])


def main():
    app = QtWidgets.QApplication(sys.argv)
    calculator = Calculator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
