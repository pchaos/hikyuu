# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_HkuChangePasswordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangePasswordDialog(object):
    def setupUi(self, ChangePasswordDialog):
        ChangePasswordDialog.setObjectName("ChangePasswordDialog")
        ChangePasswordDialog.resize(393, 204)
        self.buttonBox = QtWidgets.QDialogButtonBox(ChangePasswordDialog)
        self.buttonBox.setGeometry(QtCore.QRect(20, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(ChangePasswordDialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 331, 111))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.old_password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.old_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_password_lineEdit.setObjectName("old_password_lineEdit")
        self.gridLayout.addWidget(self.old_password_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.new_password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.new_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_password_lineEdit.setObjectName("new_password_lineEdit")
        self.gridLayout.addWidget(self.new_password_lineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.confirm_password_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.confirm_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_lineEdit.setObjectName("confirm_password_lineEdit")
        self.gridLayout.addWidget(self.confirm_password_lineEdit, 2, 1, 1, 1)

        self.retranslateUi(ChangePasswordDialog)
        self.buttonBox.accepted.connect(ChangePasswordDialog.accept)
        self.buttonBox.rejected.connect(ChangePasswordDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChangePasswordDialog)

    def retranslateUi(self, ChangePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        ChangePasswordDialog.setWindowTitle(_translate("ChangePasswordDialog", "Dialog"))
        self.label.setText(_translate("ChangePasswordDialog", "Old password"))
        self.label_2.setText(_translate("ChangePasswordDialog", "New password"))
        self.label_3.setText(_translate("ChangePasswordDialog", "Repeat new password"))