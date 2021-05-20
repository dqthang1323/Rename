from PyQt5 import QtCore, QtGui, QtWidgets, uic
from os import rename, listdir
import os
def rename():
    path = call.path_text.text()
    name_film = call.name_film.text()
    type_file = call.type_file.text()

    os.chdir(path)
    i = 1
    for file in os.listdir():
        src = file
        dst = dst = str(i) + " " + name_film + "." + type_file
        os.rename(src,dst)
        i+=1
    
    # print(name_film)
    # print(path)
    # print(type_file)

app = QtWidgets.QApplication([])
call = uic.loadUi("rename.ui")
call.btn_rename.clicked.connect(rename)
call.show()
app.exec()