import sys
from PySide2 import QtCore, QtGui, QtWidgets
from view import Ui_Dialog
from vkBot import VkBot

app = QtWidgets.QApplication(sys.argv)

Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


def bot():
    token = "188be88e1f6e543df9f5aa58ec93ae79a0313b67f1522cb4676f58b6b18a173c3d6383ee0fa70fdd2958d"
    bot = VkBot(token)
    bot.runBot()


ui.pushButton_2.clicked.connect(bot)

sys.exit(app.exec_())
