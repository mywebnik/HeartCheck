# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QPushButton, QLabel, QLineEdit

from instr import *  #загружаем переменные из файла instr.py
from final_win import *

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear() # устанавливает, как будет выглядеть окно
        self.initUI() # создаём и настраиваем графические элементы
        self.connects() # устанавливает связи между элементами
        self.show()  # показываем окно
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_sendresults, self)
        self.btn_test1 = QPushButton(txt_starttest1, self)
        self.btn_test2 = QPushButton(txt_starttest2, self)
        self.btn_test3 = QPushButton(txt_starttest3, self)

        self.text_name = QLabel(txt_name)
        self.text_age = QLabel(txt_age)
        self.text_test1 = QLabel(txt_test1)
        self.text_test2 = QLabel(txt_test2)
        self.text_test3 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)

        self.line_name = QLineEdit(txt_hintname)
        self.line_age = QLineEdit(txt_hintage)
        self.line_test1 = QLineEdit(txt_hinttest1)
        self.line_test2 = QLineEdit(txt_hinttest2)
        self.line_test3 = QLineEdit(txt_hinttest3)

        self.l_line = QVBoxLayout()
        self.r_line = QVBoxLayout()
        self.h_line = QHBoxLayout()
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft) 
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter) 
        self.h_line.addLayout(self.l_line)  
        self.h_line.addLayout(self.r_line)        
        self.setLayout(self.h_line)
    def next_click(self):
        self.hide()
        self.fw = FinalWin()
        
    def timer_test1(self): #функция-обработчик для кнопки для 1-го теста
        global time # обьявляем глобальную переменную в которой будет хранить обект время1
        time = QTime(0, 0, 15) # создаем объект для хранения времени1
        self.timer = QTimer() # создаем таймер1
        self.timer.timeout.connect(self.timer1Event)  #привязываем к таймеру1 функцию- обработчик timer1Event()
        self.timer.start(1000)  #запускаем работу таймера
    def timer1Event(self): #функция обработчик меняющая таймер1
        global time
        time = time.addSecs(-1) #уменьшаем хранимое время1 на 1 секунду 
        self.text_timer.setText(time.toString("hh:mm:ss"))  # на виджете Qlabel text_timer меняем текст - отображаем время1 в нужном виде
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold)) # на виджете Qlabel text_timer меняем меняем шрифт на нужный нам
        self.text_timer.setStyleSheet("color: rgb(0,0,0)") # на виджете Qlabel text_timer меняем меняем цвет на нужный нам
        if time.toString("hh:mm:ss") == "00:00:00":  # если время1 достигает 0
            self.timer.stop() # останавливаем работу таймера

    def timer_sits(self):
        global time # обьявляем глобальную переменную в которой будет хранить обект время2
        time = QTime(0, 0, 30)
        self.timer = QTimer() # создаем таймер2
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)  #запускаем работу таймера2 через 1500 мс
    def timer2Event(self):
        global time
        time = time.addSecs(-1) #уменьшаем хранимое время2 на 1
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])  # на виджете Qlabel text_timer меняем текст - отображаем время2 в нужном виде
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold)) # на виджете Qlabel text_timer меняем меняем шрифт на нужный нам
        self.text_timer.setStyleSheet("color: rgb(0,0,0)") # на виджете Qlabel text_timer меняем меняем цвет на нужный нам
        if time.toString("hh:mm:ss") == "00:00:00":  # если время2 достигает 0
            self.timer.stop() # останавливаем работу таймера
        
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
        self.btn_test1.clicked.connect(self.timer_test1)  #привязываем к кнопке btn_test1 функцию timer_test1()
        self.btn_test2.clicked.connect(self.timer_sits)  #привязываем к кнопке btn_test2 функцию timer_sits()

app = QApplication([])
tw = TestWin()
app.exec()
