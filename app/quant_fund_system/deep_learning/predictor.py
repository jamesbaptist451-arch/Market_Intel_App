from tensorflow.keras.models import load_model
import numpy as np

class LSTMPredictor:

    def __init__(self):
        self.model = load_model("lstm_quant_model.h5")

    def predict(self, sequence):
        sequence = np.expand_dims(sequence, axis=0)
        return float(self.model.predict(sequence)[0][0])
