# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main_uilNPagy.ui'
##
# Created by: Qt User Interface Compiler version 6.5.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
                               QLabel, QLineEdit, QPlainTextEdit, QPushButton,
                               QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
                               QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1103, 543)
        Form.setStyleSheet(
            u"background-color: rgb(49, 52, 54); color: rgb(23, 162, 184)")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 10, 271, 31))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(6, 70, 262, 431))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelID = QLabel(self.layoutWidget)
        self.labelID.setObjectName(u"labelID")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.labelID.setFont(font1)

        self.horizontalLayout.addWidget(self.labelID)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lineEditID = QLineEdit(self.layoutWidget)
        self.lineEditID.setObjectName(u"lineEditID")
        self.lineEditID.setStyleSheet(
            u"background-color: black; border: 1px solid rgb(23, 162, 184)")

        self.horizontalLayout.addWidget(self.lineEditID)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelDate = QLabel(self.layoutWidget)
        self.labelDate.setObjectName(u"labelDate")
        self.labelDate.setFont(font1)

        self.horizontalLayout_2.addWidget(self.labelDate)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"border: 1px solid rgb(23, 162, 184)")
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelTitle = QLabel(self.layoutWidget)
        self.labelTitle.setObjectName(u"labelTitle")
        self.labelTitle.setFont(font1)

        self.horizontalLayout_3.addWidget(self.labelTitle)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lineEditTitle = QLineEdit(self.layoutWidget)
        self.lineEditTitle.setObjectName(u"lineEditTitle")
        self.lineEditTitle.setEnabled(True)
        self.lineEditTitle.setStyleSheet(
            u"background-color:  black; border: 1px solid rgb(23, 162, 184)")

        self.horizontalLayout_3.addWidget(self.lineEditTitle)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelLink = QLabel(self.layoutWidget)
        self.labelLink.setObjectName(u"labelLink")
        self.labelLink.setFont(font1)

        self.horizontalLayout_4.addWidget(self.labelLink)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lineEditLink = QLineEdit(self.layoutWidget)
        self.lineEditLink.setObjectName(u"lineEditLink")
        self.lineEditLink.setStyleSheet(
            u"background-color:  black; border: 1px solid rgb(23, 162, 184)")

        self.horizontalLayout_4.addWidget(self.lineEditLink)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelDescription = QLabel(self.layoutWidget)
        self.labelDescription.setObjectName(u"labelDescription")
        self.labelDescription.setFont(font1)

        self.verticalLayout_2.addWidget(self.labelDescription)

        self.plainTextEditDescription = QPlainTextEdit(self.layoutWidget)
        self.plainTextEditDescription.setObjectName(
            u"plainTextEditDescription")
        self.plainTextEditDescription.setStyleSheet(
            u"background-color:  black; border: 1px solid rgb(23, 162, 184)")

        self.verticalLayout_2.addWidget(self.plainTextEditDescription)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.pushButtonAddData = QPushButton(self.layoutWidget)
        self.pushButtonAddData.setObjectName(u"pushButtonAddData")
        self.pushButtonAddData.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.pushButtonAddData)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(292, 72, 791, 431))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelTable = QLabel(self.layoutWidget1)
        self.labelTable.setObjectName(u"labelTable")
        self.labelTable.setFont(font1)

        self.verticalLayout_5.addWidget(self.labelTable)

        self.tableViewData = QTableView(self.layoutWidget1)
        self.tableViewData.setObjectName(u"tableViewData")
        self.tableViewData.setStyleSheet(
            u"background-color: \"black\"; border: 1px solid rgb(23, 162, 184)")
        self.tableViewData.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_5.addWidget(self.tableViewData)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButtonDeleteData = QPushButton(self.layoutWidget1)
        self.pushButtonDeleteData.setObjectName(u"pushButtonDeleteData")
        self.pushButtonDeleteData.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.pushButtonDeleteData)

        self.horizontalSpacer_8 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.pushButtonEditData = QPushButton(self.layoutWidget1)
        self.pushButtonEditData.setObjectName(u"pushButtonEditData")
        self.pushButtonEditData.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.pushButtonEditData)

        self.horizontalSpacer_9 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.pushButtonClearAll = QPushButton(self.layoutWidget1)
        self.pushButtonClearAll.setObjectName(u"pushButtonClearAll")
        self.pushButtonClearAll.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.pushButtonClearAll)

        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate(
            "Form", u"Felv\u00e9tel nyilv\u00e1ntart\u00f3", None))
        self.label.setText(QCoreApplication.translate(
            "Form", u"Felv\u00e9tel nyilv\u00e1ntart\u00f3 rendszer", None))
        self.labelID.setText(QCoreApplication.translate(
            "Form", u"Sorsz\u00e1m:", None))
        self.labelDate.setText(QCoreApplication.translate(
            "Form", u"D\u00e1tum:", None))
        self.labelTitle.setText(
            QCoreApplication.translate("Form", u"C\u00edm:", None))
        self.labelLink.setText(
            QCoreApplication.translate("Form", u"Link:", None))
        self.labelDescription.setText(
            QCoreApplication.translate("Form", u"Le\u00edr\u00e1s:", None))
        self.pushButtonAddData.setText(QCoreApplication.translate(
            "Form", u"Adatok hozz\u00e1ad\u00e1s", None))
        self.labelTable.setText(QCoreApplication.translate(
            "Form", u"Nyilv\u00e1ntart\u00f3 adatok", None))
        self.pushButtonDeleteData.setText(QCoreApplication.translate(
            "Form", u"Adatok t\u00f6rl\u00e9se", None))
        self.pushButtonEditData.setText(QCoreApplication.translate(
            "Form", u"Adatok szerkeszt\u00e9se", None))
        self.pushButtonClearAll.setText(QCoreApplication.translate(
            "Form", u"\u00d6sszes adat t\u00f6rl\u00e9s", None))
    # retranslateUi
