# LIBRARIES
import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import pandas as pd
# UTILITIES
import Utilities.DropAudio as dropAudio
import Utilities.LoadAudio as load
import Utilities.Descriptors as descriptors

# MAIN CLASS
class Main(QMainWindow, QWidget):

    # CREATE AND SET MIXER
    def __init__(self):
        super().__init__()

        # GLOBAL SIZE
        self.globalWidth = 600
        self.globalHeight = 260
        self.resize(self.globalWidth, self.globalHeight)

        # GLOBAL DATA
        self.samples = []
        self.sr = []

        # CREAR INTERFAZ
        self.createGUI()

        # MODELO
        self.model = pickle.load(open('InstrumentsClassifier/Models/randomForest_Model.sav', 'rb'))

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

        # PREDICTION
        self.title = QLabel(self)
        self.title.setText("CARGA UN SONIDO PARA PREDECIR...")
        self.title.setFont(QFont('Nixie One', 20))
        self.title.setGeometry(int(self.globalWidth/2 - 190), 200, 380, 30)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

    def printPrediction(self, inResul):
        self.title.setText(inResul)

    def makePrediction(self):
        self.loadAudio()

        data = self.getData()
        resul = self.predict(data)
        
        self.interpret(resul)

    def loadAudio(self):
        path = QListWidgetItem(self.box.item(0))
        if path.text():
            self.samples, self.sr = load.loadAudio(path.text(), inConfig="mono")

    def getData(self):
        print("------------------")
        print("Obteniendo data...")
        # IN FREQUENCY DOMAIN
        descriptorsData = []
        descriptorsLabels = ['Centroid_Freq', 'Spread_Freq', 'Peak_Freq', 'Centroid_Time', 'Slope', 'MFCC_1', 'MFCC_2', 'MFCC_3', 'MFCC_4', 'MFCC_5', 'MFCC_6', 'MFCC_7', 'MFCC_8', 'MFCC_9', 'MFCC_10', 'MFCC_11', 'MFCC_12', 'MFCC_13']
        spectrum = descriptors.getSpectrum(self.samples)
        frequency = descriptors.getFrequency(self.samples, self.sr)

        descriptorsData.append(descriptors.getCentroid(frequency, spectrum))
        descriptorsData.append(descriptors.getSpread(frequency, spectrum))
        descriptorsData.append(descriptors.getPeak(frequency, spectrum))

        time = descriptors.getVectorTime(self.samples, self.sr)
        descriptorsData.append(descriptors.getCentroid(time, self.samples))
        descriptorsData.append(descriptors.getSlope(self.samples, self.sr))
        for mfcc in descriptors.getMFCC(self.samples, self.sr):
            descriptorsData.append(mfcc.mean())

        datos = pd.DataFrame([descriptorsData], columns=descriptorsLabels)
        return datos

    def predict(self, inData):
        print("------------------")
        print("Prediciendo...")
        result = self.model.predict(inData)
        
        return result

    def interpret(self, inResul):
        print("------------------")
        print("Interpretando...")

        inResul = inResul[0]
        resul = ""

        if inResul == 1:
            print("El modelo predijo un kick")
            resul = "Es un kick"
        elif inResul == 2:
            print("El modelo predijo un snare")
            resul = "Es un snare"
        elif inResul == 3:
            print("El modelo predijo un hihat")
            resul = "Es un hihat"
        elif inResul == 4:
            print("El modelo predijo una guitarra")
            resul = "Es una guitarra"
        elif inResul == 5:
            print("El modelo predijo un bass")
            resul = "Es un bass"
        elif inResul == 6:
            print("El modelo predijo una voz")
            resul = "Es una voz"
        else:
            print("Error")
            resul = "Error"

        self.printPrediction(resul)
        self.box.clear()

# EXECUTATE PROGRAM
app = QApplication(sys.argv)
demo = Main()
demo.show()
sys.exit(app.exec_())

