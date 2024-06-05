# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:19:08 2024

@author: matteopicciolini
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget,QTableWidgetItem
from PyQt5 import uic
import sys
 
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi(r"ui/mainwindow.ui", self)

        self.button = self.findChild(QPushButton, "pushProfs")


        
        self.show()
 
    def chargeProfs(self):

        profDictionary={}

    	fileIn=open("input/docenti.csv", "r", encoding="utf-8")
        der = csv.DictReader(fileIn)

    	dati = []

    	for prova in reader:
            dati.append(prova)
        fileIn.close()
 
        print(dati)


        
app = QApplication(sys.argv)
window = UI()
app.exec_()