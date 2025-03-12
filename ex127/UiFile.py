from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 585)
        MainWindow.setStyleSheet("background-color: #2c3e50;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 671, 421))
        self.tableWidget.setStyleSheet("background-color: #ecf0f1; gridline-color: #bdc3c7;")
        self.tableWidget.setObjectName("tableWidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 440, 55, 21))
        self.label.setStyleSheet("color: #ecf0f1;")
        self.label.setObjectName("label")

        self.pushButton = self.create_button(self.centralwidget, 40, 470, 93, 28, "Refresh Data", "#1abc9c")
        self.pushButton_2 = self.create_button(self.centralwidget, 180, 470, 101, 28, "Sort By Price", "#3498db")
        self.pushButton_3 = self.create_button(self.centralwidget, 312, 470, 111, 28, "Reduce by Symbol", "#e67e22")
        self.pushButton_4 = self.create_button(self.centralwidget, 460, 470, 93, 28, "USD Column", "#9b59b6")
        self.pushButton_5 = self.create_button(self.centralwidget, 600, 470, 93, 28, "Add New Row", "#e74c3c")
        self.pushButton_6 = self.create_button(self.centralwidget, 110, 520, 93, 28, "Statistics", "#f1c40f")
        self.pushButton_7 = self.create_button(self.centralwidget, 530, 520, 93, 28, "Delete", "#c0392b")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def create_button(self, parent, x, y, width, height, text, color):
        button = QtWidgets.QPushButton(parent)
        button.setGeometry(QtCore.QRect(x, y, width, height))
        button.setText(text)
        button.setStyleSheet(f"background-color: {color}; color: white; border-radius: 5px;")
        button.setObjectName(text.replace(" ", "_"))
        return button

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
