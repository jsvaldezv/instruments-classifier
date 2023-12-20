# Instruments Classifier

<img width="598" alt="classifier" src="https://user-images.githubusercontent.com/47612276/153321732-26756fec-e32b-4289-ac6c-3c5143f435bd.png">

Instruments Classifier made with Python and Scikit Learn. First I collected audios of the instruments I wanted to the model to be able to predict, then I 
generated audio descriptors such as Centroid, Peak, Spread, MFCC in time and frequency domain. Later, I used all this info in order to train a random forest
and be able to generate a model in .sav. Finally I build a little prototype with the exported model with Python and PYQT5 in order to just drop an audio and 
be able to predict which instrument is the sound.

Note: The training was performed in Jupyter lab and the prototype developed in Visual Studio Code but you should be able to run the code with spider, jupyter, pycharm or console itself as well.

### Instruments the model can predict (at the moment)

* Kick
* Snare
* HiHat
* Guitar
* Bass
* Vocal

### Dependencies

Note: I recommend install all Anaconda package in order to have a good python environment.

* Scikit Learn from https://scikit-learn.org/stable/# for machine learning
  - Python formula: ```pip install -U scikit-learn```
  
* PyQT5 from https://pypi.org/project/PyQt5/ for GUI
  - Python formula: ```pip install PyQt5```
  
* Soundfile from https://pypi.org/project/SoundFile/ for reading and writing audio
  - Python formula: ```pip install soundfile``` 

* Librosa from https://librosa.org/doc/latest/index.html for audio descriptors
  - Python formula: ```pip install librosa```

* Scipy from https://scipy.org/ for audio descriptors
  - Python formula: ```python -m pip install --user scipy```
  
* Matplotlib from https://matplotlib.org/ for audio and data visualization
  - Python formula: ```pip install matplotlib```

* Pandas from https://pandas.pydata.org/ for data manipulation
  - Python formula: ```pip install pandas```

* Seaborn from https://seaborn.pydata.org/ for data visualization
  - Python formula: ```pip install seaborn```
