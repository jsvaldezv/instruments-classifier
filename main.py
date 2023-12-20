import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import pandas as pd

import Utilities.DropAudio as dropAudio
import Utilities.LoadAudio as load
import Utilities.Descriptors as descriptors


class Main(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()

        self.globalWidth = 600
        self.globalHeight = 260
        self.resize(self.globalWidth, self.globalHeight)

        self.samples = []
        self.sr = []

        self.createGUI()

        # Model
        self.model = pickle.load(open("Models/randomForest_Model.sav", "rb"))

    def createGUI(self):
        self.title = QLabel(self)
        self.title.setText("Instruments classifier")
        self.title.setFont(QFont("Nixie One", 20))
        self.title.setGeometry(int(self.globalWidth / 2 - 170), 10, 340, 30)

        self.box = dropAudio.ListboxWidget(self)
        self.box.setBounds(int(self.globalWidth / 2 - 30), 90, 200, 50)

        self.btnPredict = QPushButton("Predict", self)
        self.btnPredict.setGeometry(120, 70, 100, 50)
        self.btnPredict.clicked.connect(lambda: self.makePrediction())

        self.btnClean = QPushButton("Clean", self)
        self.btnClean.setGeometry(120, 130, 100, 50)
        self.btnClean.clicked.connect(lambda: self.box.clear())

        self.title = QLabel(self)
        self.title.setText("Load a sample to predict...")
        self.title.setFont(QFont("Nixie One", 20))
        self.title.setGeometry(int(self.globalWidth / 2 - 190), 200, 380, 30)
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
        print("Getting data...")

        descriptorsData = []
        descriptorsLabels = [
            "Centroid_Freq",
            "Spread_Freq",
            "Peak_Freq",
            "RollOff_Freq",
            "Centroid_Time",
            "Spread_Time",
            "Peak_Time",
            "RollOff_Time",
            "MFCC_1",
            "MFCC_2",
            "MFCC_3",
            "MFCC_4",
            "MFCC_5",
            "MFCC_6",
            "MFCC_7",
            "MFCC_8",
            "MFCC_9",
            "MFCC_10",
            "MFCC_11",
            "MFCC_12",
            "MFCC_13",
        ]

        # Frequency domain
        spectrum = descriptors.getSpectrum(self.samples)
        frequency = descriptors.getFrequency(self.samples, self.sr)
        descriptorsData.append(descriptors.getCentroid(frequency, spectrum))
        descriptorsData.append(descriptors.getSpread(frequency, spectrum))
        descriptorsData.append(descriptors.getPeak(frequency, spectrum))
        descriptorsData.append(descriptors.getRollOff(frequency, spectrum))

        # Time domain
        time = descriptors.getVectorTime(self.samples, self.sr)
        descriptorsData.append(descriptors.getCentroid(time, self.samples))
        descriptorsData.append(descriptors.getSpread(time, self.samples))
        descriptorsData.append(descriptors.getPeak(time, self.samples))
        descriptorsData.append(descriptors.getRollOff(time, self.samples))

        for mfcc in descriptors.getMFCC(self.samples, self.sr):
            descriptorsData.append(mfcc.mean())

        datos = pd.DataFrame([descriptorsData], columns=descriptorsLabels)
        return datos

    def predict(self, inData):
        print("------------------")
        print("Predicting...")
        result = self.model.predict(inData)

        return result

    def interpret(self, inResul):
        print("------------------")
        print("Thinking...")

        inResul = inResul[0]
        resul = ""

        if inResul == 1:
            print("The mode predicted a kick")
            resul = "It is a kick"
        elif inResul == 2:
            print("The mode predicted a snare")
            resul = "It is a snare"
        elif inResul == 3:
            print("The mode predicted a hihat")
            resul = "It is a hihat"
        elif inResul == 4:
            print("The mode predicted a guitar")
            resul = "It is a guitar"
        elif inResul == 5:
            print("The mode predicted a bass")
            resul = "It is a bass"
        elif inResul == 6:
            print("The mode predicted a voz")
            resul = "It is a vox"
        else:
            print("Error")
            resul = "Error"

        self.printPrediction(resul)
        self.box.clear()


app = QApplication(sys.argv)
demo = Main()
demo.show()
sys.exit(app.exec_())
