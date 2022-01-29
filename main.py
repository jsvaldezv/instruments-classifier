# LIBRARIES
import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# UTILITIES
import Utilities.DropAudio as dropAudio
import Utilities.LoadAudio as load

# MAIN CLASS
class Main(QMainWindow, QWidget):

    # CREATE AND SET MIXER
    def __init__(self):
        super().__init__()

        # GLOBAL SIZE
        self.globalWidth = 600
        self.globalHeight = 600
        self.resize(self.globalWidth, self.globalHeight)

        # GLOBAL DATA
        self.track = []
        self.sr = []

        # CREAR INTERFAZ
        self.createGUI()

    def createGUI(self):
        # TITLE
        self.title = QLabel(self)
        self.title.setText("CLASIFICADOR DE INSTRUMENTOS")
        self.title.setFont(QFont('Nixie One', 20))
        self.title.setGeometry(int(self.globalWidth/2 - 170), 10, 340, 30)
        
        # INSTRUMENT BOX
        self.box = dropAudio.ListboxWidget(self)
        self.box.setBounds(int(self.globalWidth/2 - 30), 90, 200, 50)

        # LOAD AUDIOS
        self.btnPredict = QPushButton('Predict', self)
        self.btnPredict.setGeometry(120, 70, 100, 50)
        self.btnPredict.clicked.connect(lambda: self.makePrediction())

        # DELETE AUDIOS
        self.btnClean = QPushButton('Clean', self)
        self.btnClean.setGeometry(120, 130, 100, 50)
        self.btnClean.clicked.connect(lambda: self.box.clear())

    def makePrediction(self):
        self.loadAudio()
        self.getData()

    def loadAudio(self):
        path = QListWidgetItem(self.box.item(0))
        if path.text():
            self.track, self.sr = load.loadAudio(path.text(), inConfig="mono")

    def getData(self):
        

# EXECUTATE PROGRAM
app = QApplication(sys.argv)
demo = Main()
demo.show()
sys.exit(app.exec_())

#model = pickle.load(open('Models/randomForest_Model.sav', 'rb'))
#result = model.score(X_test, Y_test)
#print(result)