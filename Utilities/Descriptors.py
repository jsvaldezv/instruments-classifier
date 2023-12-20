import numpy as np
import math
from scipy.fft import rfftfreq, rfft
import librosa


def getVectorTime(inSamples, inSampleRate):
    return np.arange(0, len(inSamples), 1) / inSampleRate


def getSpectrum(inSamples):
    return np.abs(rfft(inSamples))


def getFrequency(inSamples, inSampleRate):
    return rfftfreq(len(inSamples), 1 / inSampleRate)


def getCentroid(inX, inY):
    return np.sum(inY * inX) / np.sum(inY)


def getSpread(inX, inY):
    centroid = getCentroid(inX, inY)
    return math.sqrt(np.abs(np.sum((inX - centroid) ** 2 * inY) / np.sum(inY)))


def getPeak(inX, inY):
    peakIndex = np.argmax(np.array(inY))
    return inX[peakIndex]


def getSlope(inSamples, inSampleRate):
    amplitude = np.abs(rfft(inSamples))
    frequency = rfftfreq(len(inSamples), 1 / inSampleRate)
    slope = np.sum(
        (amplitude - amplitude.mean()) * (frequency - frequency.mean())
    ) / np.sum((frequency - frequency.mean()) ** 2)
    return slope


def getMFCC(inSamples, inSampleRate):
    mfccValue = librosa.feature.mfcc(inSamples, sr=inSampleRate, n_mfcc=13)
    return mfccValue


def getRollOff(inX, inY, treshold=0.95):
    cumsum = np.cumsum(inY)
    cont = 0
    rolloff = 0
    for accum in cumsum:
        if accum > (cumsum[-1] * treshold):
            rolloff = inX[cont]
            break
        cont += 1
    return rolloff
