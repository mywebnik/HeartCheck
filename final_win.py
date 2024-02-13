# напиши здесь код третьего экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit

from instr import *  #загружаем переменные из файла instr.py

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.show()  # показываем окно
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.layout = QVBoxLayout()
        self.index_text = QLabel(txt_index)
        self.workheart_text = QLabel(txt_workheart)
        self.layout.addWidget(self.index_text)
        self.layout.addWidget(self.workheart_text)
        self.setLayout(self.layout)
    def initUI(self):
        ''' создает графические элементы '''
        self.workh_text = QLabel(txt_workheart)
        self.index_text = QLabel(txt_index)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
        self.layout_line.addWidget(self.workh_text, alignment = Qt.AlignCenter)         
        self.setLayout(self.layout_line)

    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
