# Instrument Classifier

<img width="598" alt="classifier" src="https://user-images.githubusercontent.com/47612276/153321732-26756fec-e32b-4289-ac6c-3c5143f435bd.png">

This project is an instrument classifier developed in Python using Scikit-learn and PyQt5. The model is capable of identifying various musical instruments from audio samples based on extracted audio descriptors.

🎧 Workflow Overview:

- Audio Dataset Collection: Gathered recordings for six instrument classes.
- Feature Extraction: Computed audio descriptors such as:
    - Spectral Centroid
    - Spectral Peak
    - Spectral Spread
    - MFCC (in time and frequency domain)
- Model Training: Trained a Random Forest classifier using Scikit-learn.
- Model Export: Saved the trained model as a .sav file.
- Prototype Interface: Built with PyQt5, allowing users to drag and drop an audio file to classify the instrument.

🥁 Instruments the Model Can Identify:

- Kick
- Snare
- Hi-Hat
- Guitar
- Bass
- Vocal

🛠️ Development Notes:

- Model training was done in JupyterLab.
- UI prototype was built in Visual Studio Code.
- Code is compatible with Spyder, Jupyter, PyCharm, or the Python console.

This project aims to make machine learning accessible for music classification and prototyping.

## Local running

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

## Recommendations

### 1. Run black to format your files with Python coding standards
```bash
(venv) black .
```
