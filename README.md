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

## Local running

With Python 3.10+ for `|` annotations

### 1. Create venv
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
(venv) pip install -r requirements.txt
```

### 3. Run main file
```bash
(venv) python main.py
```
