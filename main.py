import sys

from PySide6 import QtCore, QtWidgets

from getProfesions import get_dict

dct = get_dict()


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Узнать")
        self.characteristic = QtWidgets.QLabel("Пусто",
                                               alignment=QtCore.Qt.AlignCenter)
        self.skills = QtWidgets.QLabel("Пусто",
                                       alignment=QtCore.Qt.AlignCenter)
        self.droplist = QtWidgets.QComboBox()
        self.droplist.addItems(dct.keys())

        self.layout = QtWidgets.QVBoxLayout(self)

        self.hor = QtWidgets.QHBoxLayout(self)
        self.hor.addWidget(self.characteristic)
        self.hor.addWidget(self.skills)


        self.layout.addLayout(self.hor)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.droplist)


        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.characteristic.setText("ЛИЧНЫЕ КАЧЕСТВА:\n" + dct[self.droplist.currentText()]["characteristic"])
        self.skills.setText("ОСНОВНЫЕ НАВЫКИ:\n" + dct[self.droplist.currentText()]["characteristic"])


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(800, 300)
    widget.show()

    sys.exit(app.exec())
