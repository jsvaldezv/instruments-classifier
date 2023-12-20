import soundfile as sf
from soundfile import SoundFile


# CHECAR MAYOR LONGITUD DE TODOS LOS AUDIOS
def checkStems(inPaths):
    mayor = 0
    # for path in inPaths:
    audio, sr = sf.read(inPaths)
    if len(audio) > mayor:
        mayor = len(audio)

    return mayor


# LOAD AUDIOS
def loadAudio(inPath, inConfig="mono"):
    print("------------------")
    print("Añadiendo track...")

    track = []
    sampleRate = 0

    audio = SoundFile(inPath)

    if inConfig == "mono":
        if audio.channels == 1:
            samples, sr = sf.read(inPath)
            track = samples
            sampleRate = sr

        else:
            samples, sr = sf.read(inPath)
            track = samples[:, 0]
            sampleRate = sr

    elif inConfig == "stereo":
        if audio.channels == 1:
            track = []
            samples, sr = sf.read(inPath)

            for sample in samples:
                track.append([sample, sample])

            sampleRate = sr

        else:
            samples, sr = sf.read(inPath)
            track = samples
            sampleRate = sr

    return track, sampleRate
