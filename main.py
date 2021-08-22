# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QInputDialog, QLineEdit
import record
import player
import macros
from threading import Thread
import sys

Recorder = record.Recorder()
Player = player.Player()
SavedFiles = macros.SavedFiles()

class Ui_MainWindow(object):

    def __init__(self):
        self.record_thread = Thread(target=Recorder.record, args=())

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Ekko")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loop_recording_button = QtWidgets.QLabel(self.centralwidget)
        self.loop_recording_button.setGeometry(QtCore.QRect(10, 290, 350, 150))
        self.loop_recording_button.setMaximumSize(QtCore.QSize(350, 150))
        self.loop_recording_button.setText("")
        self.loop_recording_button.setPixmap(QtGui.QPixmap("Play.png"))
        self.loop_recording_button.setObjectName("loop_recording_button")
        self.record_button = QtWidgets.QLabel(self.centralwidget)
        self.record_button.setGeometry(QtCore.QRect(10, 120, 350, 150))
        self.record_button.setMaximumSize(QtCore.QSize(350, 150))
        self.record_button.setText("")
        self.record_button.setPixmap(QtGui.QPixmap("RECORD (1).png"))
        self.record_button.setObjectName("record_button")
        self.load_button = QtWidgets.QLabel(self.centralwidget)
        self.load_button.setGeometry(QtCore.QRect(440, 120, 350, 250))
        self.load_button.setMaximumSize(QtCore.QSize(350, 250))
        self.load_button.setText("")
        self.load_button.setPixmap(QtGui.QPixmap("LOAD.png"))
        self.load_button.setObjectName("load_button")
        self.numbers = QtWidgets.QLabel(self.centralwidget)
        self.numbers.setGeometry(QtCore.QRect(570, 450, 101, 51))
        self.numbers.setObjectName("numbers")
        self.About = QtWidgets.QLabel(self.centralwidget)
        self.About.setGeometry(QtCore.QRect(290, 10, 93, 28))
        self.About.setMaximumSize(QtCore.QSize(93, 28))
        self.About.setObjectName("About")
        self.Instructions = QtWidgets.QLabel(self.centralwidget)
        self.Instructions.setGeometry(QtCore.QRect(420, 10, 110, 28))
        self.Instructions.setMaximumSize(QtCore.QSize(110, 28))
        self.Instructions.setObjectName("Instructions")
        self.Create = QtWidgets.QLabel(self.centralwidget)
        self.Create.setGeometry(QtCore.QRect(40, 40, 291, 51))
        self.Create.setObjectName("Create")
        self.Load = QtWidgets.QLabel(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(450, 40, 321, 51))
        self.Load.setObjectName("Load")
        self.macro_name = QtWidgets.QLabel(self.centralwidget)
        self.macro_name.setGeometry(QtCore.QRect(520, 400, 201, 51))
        self.macro_name.setObjectName("macro_name")
        self.right_button = QtWidgets.QLabel(self.centralwidget)
        self.right_button.setGeometry(QtCore.QRect(720, 400, 50, 50))
        self.right_button.setMaximumSize(QtCore.QSize(50, 50))
        self.right_button.setText("")
        self.right_button.setPixmap(QtGui.QPixmap("Right.png"))
        self.right_button.setObjectName("right_button")
        self.left_button = QtWidgets.QLabel(self.centralwidget)
        self.left_button.setGeometry(QtCore.QRect(460, 400, 50, 50))
        self.left_button.setMaximumSize(QtCore.QSize(50, 50))
        self.left_button.setText("")
        self.left_button.setPixmap(QtGui.QPixmap("Left.png"))
        self.left_button.setObjectName("left_button")
        self.save_button = QtWidgets.QLabel(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(40, 450, 100, 100))
        self.save_button.setMaximumSize(QtCore.QSize(100, 100))
        self.save_button.setText("")
        self.save_button.setPixmap(QtGui.QPixmap("Save.png"))
        self.save_button.setObjectName("save_button")
        self.delete_button = QtWidgets.QLabel(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(220, 450, 100, 100))
        self.delete_button.setMaximumSize(QtCore.QSize(100, 100))
        self.delete_button.setText("")
        self.delete_button.setPixmap(QtGui.QPixmap("Delete.png"))
        self.delete_button.setObjectName("delete_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.record_button.mouseReleaseEvent = self.record_clicked
        self.About.mouseReleaseEvent = self.about_clicked
        self.Instructions.mouseReleaseEvent = self.instructions_clicked
        self.right_button.mouseReleaseEvent = self.next_clicked
        self.left_button.mouseReleaseEvent = self.back_clicked
        self.delete_button.mouseReleaseEvent = self.delete_clicked
        self.save_button.mouseReleaseEvent = self.save_clicked
        self.load_button.mouseReleaseEvent = self.load_clicked
        self.loop_recording_button.mouseReleaseEvent = self.loop_clicked

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Ekko", "Ekko"))
        self.numbers.setText(_translate("Ekko",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" + str(
                                            SavedFiles.get_file_data()[0]) + " of " + str(SavedFiles.get_current_size()) + "</span></p></body></html>"))
        self.About.setText(_translate("Ekko",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">About</span></p></body></html>"))
        self.Instructions.setText(_translate("Ekko",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline;\">Instructions</span></p></body></html>"))
        self.Create.setText(_translate("Ekko",
                                       "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Create New Macro</span></p></body></html>"))
        self.Load.setText(_translate("Ekko",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Load Existing Macro</span></p></body></html>"))
        self.macro_name.setText(_translate("Ekko",
                                           "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">" + SavedFiles.get_file_data()[1] + "</span></p></body></html>"))

    def record_clicked(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Record Status")
        msg.setText("Ensure the correct window is open.\nClick OK or press enter to begin recording.")
        x = msg.exec_()
        if self.record_thread.is_alive():
            print("Recording thread still alive")
        else:
            self.record_thread = Thread(target=Recorder.record, args=())
            self.record_thread.start()

    def about_clicked(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("The purpose of this application is to record cursor movement and keyboard inputs which can be saved and played back any amount of times")
        x = msg.exec_()

    def instructions_clicked(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Instructions")
        msg.setText("1. When ready to record cursor movement and key presses, click the RECORD button."
                    "\n2. To stop recording press the ESC key."
                    "\n3. To play back your recording click the LOOP RECORDING button."
                    "\n4. If you wish to keep the recording, click Save Recording and name it."
                    "\n5. If you wish to discard the recording you can simply click RECORD once again."
                    "\n6. To use a previously saved recording, use the arrows to navigate to the desired macro and click LOAD.")
        x = msg.exec_()

    def delete_clicked(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Delete Status")
        msg.setText("Macro deleted!")
        SavedFiles.delete_file()
        self.macro_name.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">" +
            SavedFiles.get_file_data()[1] + "</span></p></body></html>")
        self.numbers.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" + str(
                SavedFiles.get_file_data()[0]) + " of " + str(
                SavedFiles.get_current_size()) + "</span></p></body></html>")
        x = msg.exec_()

    def save_clicked(self, text):
        name, okPressed = QInputDialog.getText(self.centralwidget, "Get text", "Your name:", QLineEdit.Normal, "")
        SavedFiles.log_to_macros(name)
        self.macro_name.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">" +
                                SavedFiles.get_file_data()[1] + "</span></p></body></html>")
        self.numbers.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" + str(
                SavedFiles.get_file_data()[0]) + " of " + str(
                SavedFiles.get_current_size()) + "</span></p></body></html>")
        msg = QMessageBox()
        msg.setWindowTitle("Save Status")
        msg.setText("Macro saved!")
        x = msg.exec_()


    def next_clicked(self, text):
        SavedFiles.to_next_file()
        self.macro_name.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">" +
            SavedFiles.get_file_data()[1] + "</span></p></body></html>")
        self.numbers.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" + str(
                SavedFiles.get_file_data()[0]) + " of " + str(SavedFiles.get_current_size()) + "</span></p></body></html>")

    def back_clicked(self, text):
        SavedFiles.to_prev_file()
        self.macro_name.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">" +
            SavedFiles.get_file_data()[1] + "</span></p></body></html>")
        self.numbers.setText(
            "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">" + str(
                SavedFiles.get_file_data()[0]) + " of " + str(SavedFiles.get_current_size()) + "</span></p></body></html>")

    def load_clicked(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("MACRO NAME")
        msg.setText("Macro loading...")
        x = msg.exec_()
        s, okPressed = QInputDialog.getText(self.centralwidget, "Number of loops", "Enter an integer number for how many times you would like the macro to run", QLineEdit.Normal, "")
        for x in range(int(s)):
            SavedFiles.play_recording(Player)
        
        

    def loop_clicked(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Playing Recording")
        msg.setText("Click OK or press enter to play recording.")
        x = msg.exec_()
        Player.play(Recorder.log_file)

sys._excepthook = sys.excepthook

def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

sys.excepthook = exception_hook

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())