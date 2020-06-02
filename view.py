# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'view.ui'
##
# Created by: Qt User Interface Compiler version 5.14.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet(u"background-color: #00d4ff;")
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 140, 221, 121))
        self.pushButton_2.setStyleSheet(u".QPushButton {\n"
                                        "	background:linear-gradient(to bottom, #79bbff 5%, #378de5 100%);\n"
                                        "	background-color:#096679;\n"
                                        "	border-radius:5px;\n"
                                        "	border:1px solid #337bc4;\n"
                                        "	color:#ffffff;\n"
                                        "}\n"
                                        ".QPushButton:hover {\n"
                                        "	background:linear-gradient(to bottom, #378de5 5%, #79bbff 100%);\n"
                                        "	background-color:#378de5;\n"
                                        "}\n"
                                        "")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 50, 175, 61))
        self.label.setStyleSheet(
            u"font: 75 22pt \"Bahnschrift SemiCondensed\";")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("Dialog", u"Bot", None))
        self.label.setText("Запустите бота")
    # retranslateUi
