import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit
from PyQt5.QtGui import QIcon 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt 

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("GUI Window")
    self.setGeometry(450, 250, 600, 500)
    self.setWindowIcon(QIcon("./gui/cat.png"))
    # PyQt5 buttons
    # self.button = QPushButton("Click me!", self)
    # self.label8 = QLabel("Hello", self)
    # PyQt5 checkboxes
    # self.checkbox = QCheckBox("Do you like cats?", self)
    # PyQt5 radio buttons
    # self.radio1 = QRadioButton("Visa", self)
    # self.radio2 = QRadioButton("MasterCard", self)
    # self.radio3 = QRadioButton("GiftCard", self)
    # self.radio4 = QRadioButton("In-Store", self)
    # self.radio5 = QRadioButton("Online", self)
    # self.button_group1 = QButtonGroup(self)
    # self.button_group2 = QButtonGroup(self)
    # PyQt5 line edits
    # self.line_edit = QLineEdit(self)
    # self.button = QPushButton("Submit", self)
    # PyQt5 CSS styles
    self.button1 = QPushButton("#1")
    self.button2 = QPushButton("#2")
    self.button3 = QPushButton("#3")
    self.initUI()

    # PyQt5 labels
    # label = QLabel("Hello", self)
    # label.setFont(QFont("Helvetica", 40))
    # label.setGeometry(0, 0, 500, 100)
    # label.setStyleSheet("color: brown;" "background-color: beige;" "font-weight: bold;" "font-style: italic;" "text-decoration: underline;")
    # # label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
    # label.setAlignment(Qt.AlignCenter)

    # PyQt5 images 
    # label2 = QLabel(self)
    # label2.setGeometry(0, 0, 250, 400)
    # pixmap = QPixmap("./gui/cat.png")
    # label2.setPixmap(pixmap)
    # label2.setScaledContents(True)
    # label2.setGeometry((self.width()-label2.width())//2, (self.height()-label2.height())//2, label2.width(), label2.height())

  # PyQt5 layout managers
  # def initUI(self):
  #   central_widget = QWidget()
  #   self.setCentralWidget(central_widget)
  #   label3 = QLabel("#1", self)
  #   label4 = QLabel("#2", self)
  #   label5 = QLabel("#3", self)
  #   label6 = QLabel("#4", self)
  #   label7 = QLabel("#5", self)

  #   label3.setStyleSheet("background-color: red;")
  #   label4.setStyleSheet("background-color: yellow;")
  #   label5.setStyleSheet("background-color: blue;")
  #   label6.setStyleSheet("background-color: green;")
  #   label7.setStyleSheet("background-color: pink;")

  #   # hbox = QHBoxLayout()
  #   # vbox = QVBoxLayout()
  #   grid = QGridLayout()

  #   grid.addWidget(label3, 0, 0)
  #   grid.addWidget(label4, 0, 1)
  #   grid.addWidget(label5, 1, 0)
  #   grid.addWidget(label6, 1, 1)
  #   grid.addWidget(label7, 2, 2)

  #   central_widget.setLayout(grid)

  # PyQt5 buttons
  # def initUI(self):
  #   self.button.setGeometry(150, 200, 200, 100)
  #   self.button.setStyleSheet("font-size: 30px;")
  #   self.button.clicked.connect(self.on_click)
  #   self.label8.setGeometry(150, 300, 200, 100)
  #   self.label8.setStyleSheet("font-size: 50px;")

  # def on_click(self):
  #   print("Button clicked!")
  #   self.button.setText("Clicked")
  #   self.button.setDisabled(True)

  #   self.label8.setText("Goodbye")

  # PyQt5 checkboxes
  # def initUI(self):
  #   self.checkbox.setStyleSheet("font-size: 30px;" "font-family: Helvetica;" )
  #   self.checkbox.setGeometry(10, 0, 500, 100)
  #   self.checkbox.setChecked(False)
  #   self.checkbox.stateChanged.connect(self. checkbox_changed)
  # def checkbox_changed(self, state):
  #   if state == Qt.Checked:
  #      print("You like cats!")
  #   else: 
  #      print("You don't like cats!")

  # PyQt5 radio buttons
  # def initUI(self):
  #   self.radio1.setGeometry(0, 0, 300, 80)
  #   self.radio2.setGeometry(0, 50, 300, 80)
  #   self.radio3.setGeometry(0, 100, 300, 80)
  #   self.radio4.setGeometry(0, 150, 300, 80)
  #   self.radio5.setGeometry(0, 200, 300, 80)

  #   self.setStyleSheet("QRadioButton{"
  #                      "font-size: 40px;"
  #                      "font-family: Helvetica;"
  #                      "padding: 10px;"
  #                      "}")
    
  #   self.button_group1.addButton(self.radio1)
  #   self.button_group1.addButton(self.radio2)
  #   self.button_group1.addButton(self.radio3)
  #   self.button_group2.addButton(self.radio4)
  #   self.button_group2.addButton(self.radio5)

  #   self.radio1.toggled.connect(self.radio_button_changed)
  #   self.radio2.toggled.connect(self.radio_button_changed)
  #   self.radio3.toggled.connect(self.radio_button_changed)
  #   self.radio4.toggled.connect(self.radio_button_changed)
  #   self.radio5.toggled.connect(self.radio_button_changed)

  # def radio_button_changed(self):
  #   radio_button = self.sender()
  #   if radio_button.isChecked():
  #     print(f"{radio_button.text()} is selected")

  # PyQt5 line edits
  # def initUI(self):
  #   self.line_edit.setGeometry(10, 10, 200, 40)
  #   self.line_edit.setStyleSheet("font-size: 25px;" "font-family: Helvetica;")
  #   self.button.setGeometry(210, 10, 100, 40)
  #   self.button.setStyleSheet("font-size: 25px;" "font-family: Helvetica;")
  #   self.line_edit.setPlaceholderText("Enter your name")
  #   self.button.clicked.connect(self.submit)

  # def submit(self):
  #   text = self.line_edit.text()
  #   print(f"Hello {text}")

  # PyQt5 CSS styles
  def initUI(self):
    central_widget = QWidget()
    self.setCentralWidget(central_widget)
    hbox = QHBoxLayout()
    hbox.addWidget(self.button1)
    hbox.addWidget(self.button2)
    hbox.addWidget(self.button3)

    central_widget.setLayout(hbox)

    self.button1.setObjectName("button1")
    self.button2.setObjectName("button2")
    self.button3.setObjectName("button3")

    self.setStyleSheet(""" QPushButton{
                      font-size: 40px;
                      font-family: Arial;
                      padding: 15px 75px;
                      margin: 25px;
                      border: 3px solid;
                      border-radius: 15px;
                      }
                      QPushButton#button1{
                        background-color: red;
                      }
                      QPushButton#button2{
                        background-color: green;
                      }
                      QPushButton#button3{
                        background-color: purple;
                      }
                       QPushButton#button1:hover{
                        background-color: orange;
                      }
                      QPushButton#button2:hover{
                        background-color: lightgreen;
                      }
                      QPushButton#button3:hover{
                        background-color: pink;
                      }
                      """)


def main():
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
  main()