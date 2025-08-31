import sys


from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Widgets App")


        layout = QVBoxLayout()
        layout.addWidget(QCheckBox())
        layout.addWidget(QComboBox())
        layout.addWidget(QDateEdit())
        layout.addWidget(QDateTimeEdit())
        layout.addWidget(QDial())
        layout.addWidget(QDoubleSpinBox())
        layout.addWidget(QFontComboBox())
        layout.addWidget(QLCDNumber())
        etiket1 = QLabel("Label aracı")
        font = etiket1.font()
        font.setPointSize(30)
        font.setOverline(True)
        etiket1.setFont(font) #
        layout.addWidget(etiket1)
        layout.addWidget(QLineEdit())
        layout.addWidget(QProgressBar())
        ss = QPushButton("SİL")
        xx = QPushButton("Güncelle")
        layout.addWidget(ss)
        layout.addWidget(xx)
        def tiklama():
            etiket1.setText("Merhaba") #değer değiştirme
            print("Düğmeye tıladın")
        ss.clicked.connect(tiklama)
        xx.clicked.connect(self.tiklama1)
        layout.addWidget(QRadioButton())
        layout.addWidget(QSlider())
        layout.addWidget(QSpinBox())
        layout.addWidget(QTimeEdit())


        widget = QWidget()
        widget.setLayout(layout)


        self.setCentralWidget(widget)
    def tiklama1(self):
        print("1 numaralı düğmeye tıklandı.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()




