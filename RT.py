#IMPORTS
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QRadioButton, QPushButton, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout
from random import randint
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIntValidator
import sys

#WINDOW THINGS
app = QApplication([])
window = QWidget()

window.setWindowTitle("Ruffier Test")
window.resize(550,550)

#layout
main_layout = QVBoxLayout()

#Screen 1
screen1 = QVBoxLayout()

scr1_widgets = {
    "title" : QLabel("Rufiers Test"),
    "description" : QLabel("It's a cardiovascular endurance test. Click -Start- to begin."),
    "start_button" : QPushButton("Start")
}

scr1_widgets["start_button"].setStyleSheet("background-color : lightpink")

for s1w in scr1_widgets.values():
    screen1.addWidget(s1w)

def start():
    scr2.show()
scr1_widgets["start_button"].clicked.connect(start)

#Screen 2
screen2 = QVBoxLayout()
scr2_widgets = {
    "name_label" : QLabel("Enter your full name:"),
    "name_input" : QLineEdit(),
    "age_label" : QLabel("Enter your age"),
    "age_input": QLineEdit(),
    "instructions1" : QLabel("#1. Lie on your back & take your pulse for 15 seconds. Click the 'Start first test' button to start the timer. Write down the result in the appropriate field."),
    "test_1" : QPushButton("Start the first test"),
    "p1_input" : QLineEdit(),
    "instructions2" : QLabel("#2. Perform 30 squats in 45 seconds. To do this, click the 'Start doing squats' button to start the squat counter."),
    "test_2": QPushButton("Start doing squats"),
    "instructions3" : QLabel("#3. Lie on your back and take your pulse for the first 15 secs of the Min, then for the last 15 secs of the min. Press 'Start final test' button to start the timer."),
    "test_3" : QPushButton("Start the final test"),
    "p2_input" : QLineEdit(),
    "p3_input" : QLineEdit(),
    "result_button" : QPushButton("Send Results")
}

scr2_widgets["age_input"].setValidator(QIntValidator())
scr2_widgets["p1_input"].setValidator(QIntValidator())
scr2_widgets["p2_input"].setValidator(QIntValidator())
scr2_widgets["p3_input"].setValidator(QIntValidator())

scr2_widgets["test_1"].setStyleSheet("background-color : yellow")
scr2_widgets["test_2"].setStyleSheet("background-color : lightgreen")
scr2_widgets["test_3"].setStyleSheet("background-color : skyblue")
scr2_widgets["result_button"].setStyleSheet("background-color : violet")
scr2_widgets["result_button"].setGeometry(200, 150, 100, 40) 

for s2w in scr2_widgets.values():
    screen2.addWidget(s2w)

#TIMERS/TIME --> Screen 2
timer_label = QLabel("Timer")
timer_label.setFont(QFont("Comic Sans MS",24,QFont.Bold))
screen2.addWidget(timer_label)
time = QTime(0,0,1)
timer = None

def startTimer1():
    global time, timer
    time = QTime(0,0,6)
    timer = QTimer()
    timer.timeout.connect(timer1)
    timer.start(1000)

def timer1():
     global time,timer
     print(f"timer counting: {time}")
     time = time.addSecs(-1)
     timer_label.setText(f'Count pulse :{time.toString("mm:ss")}')
     if time.toString("mm:ss") == "00:00":
          timer.stop()
          timer_label.setText('Enter pulse, then begin test #2.')
scr2_widgets["test_1"].clicked.connect(startTimer1)

def startTimer2():
    global time, timer
    time = QTime(0,0,0)
    timer = QTimer()
    timer.timeout.connect(timer2)
    timer.start(1500)

squat = 0
def timer2():
    global timer, squat
    squat += 1
    timer_label.setText(f'SQUAT: {squat}')
    if squat == 5:
        timer.stop()
        timer_label.setText("Begin test #3.")
scr2_widgets["test_2"].clicked.connect(startTimer2)

def startTimer3():
    pass


def results():
    scr1.hide()
    scr2.hide()
    scr3.show()
scr2_widgets["result_button"].clicked.connect(results)

#Screen 3
screen3 = QVBoxLayout()
scr3_widgets = {
    "results_intro" : QLabel("Here are your results: "),
    "rufier_index" : QLabel("Rufier Index : 0"),
    "cardiac_performance" : QLabel("Cardiac performance: there is no data for this age")
}
for s3w in scr3_widgets.values():
    screen3.addWidget(s3w)

#Screen 3 Interface

scr1 = QGroupBox()
scr2 = QGroupBox()
scr3 = QGroupBox()

scr1.setLayout(screen1)
scr2.setLayout(screen2)
scr3.setLayout(screen3)

main_layout.addWidget(scr1)
main_layout.addWidget(scr2)
main_layout.addWidget(scr3)

scr1.show()
scr2.hide()
scr3.hide()

#END
window.setLayout(main_layout)
window.show()
app.exec_()