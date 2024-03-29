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
    "description" : QLabel("The Ruffier test is a 3-minute heart rate test. This simple test requires participants to perform 30 squats in 45 seconds. Give it a shot! Click -Start- to begin."),
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
timer_label.setFont(QFont("Comic Sans MS",22,QFont.Bold))
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
    if squat == 4:
        timer.stop()
        timer_label.setText("Begin test #3.")
scr2_widgets["test_2"].clicked.connect(startTimer2)


def startTimer3():
    global time, timer
    time = QTime(0,0,4)
    timer = QTimer()
    timer.timeout.connect(timer3)
    timer.start(1000)

def timer3():
    global timer, time
    time = time.addSecs(-1)
    timer_label.setText(time.toString("mm:ss"))
    if int(time.toString("ss")) >= 6:
        timer_label.setStyleSheet("color: rgb(102, 0, 255)")
    elif int(time.toString("ss")) <= 4:
        timer_label.setStyleSheet("color: rgb(102, 0, 255)")
    else:
        timer_label.setStyleSheet("color: rgb(0,0,0)")
    if time.toString("mm:ss") == "00:00":
        timer.stop()
        timer_label.setText('Enter the results for test #2 & #3.')
scr2_widgets["test_3"].clicked.connect(startTimer3)


index = 0
ur_level = ""
def results():
    global index
    global ur_level

    msg_box = QMessageBox()
    msg_box1 = QMessageBox()
    msg_box2 = QMessageBox()
    msg_box3 = QMessageBox()
    if scr2_widgets["age_input"].text() == "":
        msg_box.setText("You must enter your Age!")
        msg_box.exec()
        return
    if scr2_widgets["p1_input"].text() == "":
        msg_box1.setText("Enter the Input for P1!")
        msg_box1.exec()
        return
    if scr2_widgets["p2_input"].text() == "":
        msg_box2.setText("Enter the Input for P2!")
        msg_box2.exec()
        return
    if scr2_widgets["p3_input"].text() == "":
        msg_box3.setText("Enter the Input for P3!")
        msg_box3.exec()
        return

    p1 = int(scr2_widgets["p1_input"].text())
    p2 = int(scr2_widgets["p2_input"].text())
    p3 = int(scr2_widgets["p3_input"].text())
    index = (4 * (p1 + p2 + p3)-200)/10
    age = int(scr2_widgets["age_input"].text())
    scr3_widgets["rufier_index"].setText("Rufier Index : " + str(index))

    scr1.hide()
    scr2.hide()
    scr3.show()

    if (age == 7 or age == 8):
        if index >= 21:
            ur_level = "Low. See your doctor ASAP! 🩺"
        if index >= 17 and index <= 20.9:
            ur_level = "Satisfactory. See your doctor. 👩‍⚕️"
        if index >= 12 and index <= 16.9:
            ur_level = "Average. May be better to go check it out. 🍎"
        if index >= 6.5 and index <= 11.9:
            ur_level = "Above Average. You're good to go. 👍"
        if index <= 6.4:
            ur_level = "High"

    if (age == 9 or age == 10):
        if index >= 19.5:
            ur_level = "Low. See your doctor ASAP! 🩺"
        if index >= 15.5 and index <= 19.4:
            ur_level = "Satisfactory. See your doctor. 👩‍⚕️"
        if index >= 10.5 and index <= 15.4:
            ur_level = "Average. May be better to go check it out. 🍎"
        if index >= 5 and index <= 10.4:
            ur_level = "Above Average. You're good to go. 👍"
        if index <= 4.9:
            ur_level = "High"

    if age == 11 or age == 12:
        if index >= 18:
            ur_level = "Low. See your doctor ASAP! 🩺"
        if index >= 14 and index <= 17.9:
            ur_level = "Satisfactory. See your doctor. 👩‍⚕️"
        if index >= 9 and index <= 13.9:
            ur_level = "Average. May be better to go check it out. 🍎"
        if index >= 3.5 and index <= 8.9:
            ur_level = "Above Average. You're good to go. 👍"
        if index <= 3.4:
            ur_level = "High"

    if age == 13 or age == 14:
        if index >= 16.5:
            ur_level = "Low. See your doctor ASAP! 🩺"
        if index >= 12.5 and index <= 16.4:
            ur_level = "Satisfactory. See your doctor. 👩‍⚕️"
        if index >= 7.5 and index <= 12.4:
            ur_level = "Average. May be better to go check it out. 🍎"
        if index >= 2 and index <= 7.4:
            ur_level = "Above Average. You're good to go. 👍"
        if index <= 1.9:
            ur_level = "High"

    if age >= 15:
        if index >= 15:
            ur_level = "Low. See your doctor ASAP! 🩺"
        if index >= 11 and index <= 14.9:
            ur_level = "Satisfactory. See your doctor. 👩‍⚕️"
        if index >= 6 and index <= 10.9:
            ur_level = "Average. May be better to go check it out. 🍎"
        if index >= 0.5 and index <= 5.9:
            ur_level = "Above Average. You're good to go. 👍"
        if index <= 0.4:
            ur_level = "High"

    scr3_widgets["cardiac_performance"].setText("Cardiac Performance : " + ur_level)

scr2_widgets["result_button"].clicked.connect(results)

#Screen 3
screen3 = QVBoxLayout()
scr3_widgets = {
    "results_intro" : QLabel("Here are your results: "),
    "rufier_index" : QLabel("Rufier Index : "),
    "cardiac_performance" : QLabel("Cardiac performance: ")
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