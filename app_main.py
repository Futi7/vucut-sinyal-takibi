from PyQt5 import QtCore, QtGui, QtWidgets
from realtime_updater import realtime_updater
import multiprocessing
from multiprocessing import Process
from subprocess import Popen, PIPE
import os


class Ui_Main(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(621, 471)
        Dialog.setStyleSheet("background: #9392e7;")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(200, 200, 221, 101))
        self.start.setStyleSheet("color: #fff;\n"
" background-color: #28a745;\n"
" border-color: #28a745;")
        self.start.setObjectName("start")


        self.stop = QtWidgets.QPushButton(Dialog)
        self.stop.setGeometry(QtCore.QRect(200, 200, 221, 101))
        self.stop.setStyleSheet("color: #fff;\n"
  "background-color: #dc3545;;\n"
  "border-color: #dc3545;;\n")
        self.stop.setObjectName("stop")



        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(245, 110, 122, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 160, 301, 31))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)







        multiprocessing.freeze_support()

        self.updater = realtime_updater(self.username)

        self.start.clicked.connect(self.start_magnum_opus)
        self.stop.clicked.connect(self.stop_magnum_opus)







    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Vücut Sinyali Ölçümü"))
        self.start.setText(_translate("Dialog", "Ölçümleri başlat"))
        self.stop.setText(_translate("Dialog", "Ölçümleri durdur"))
        self.stop.hide()
        self.label.setText(_translate("Dialog", "Merhaba "+ self.username))
        self.label_2.setText(_translate("Dialog", "Ölçümlere başlamak için lütfen butona basın"))




    def start_magnum_opus(self):
        self.start.hide()
        self.stop.show()
        self.label_2.setText("Ölçümlere durdurmak için lütfen butona basın")
        self.p1 = Process(target=self.updater.start)
        self.proc = Popen(['python2', 'mi_band_com.py', 'C3:2A:EC:6C:90:B9'], stdout=PIPE, bufsize=0)
        self.p1.start()
        

    def stop_magnum_opus(self):
        self.stop.hide()
        self.start.show()
        self.proc.kill()
        self.p1.kill()



    def setValue(self, username):
        self.username = username
    
