import joblib

class MLInference:

    def __init__(self):
        self.model = joblib.load("institutional_model.pkl")

    def predict(self, features):
        return self.model.predict_proba([features])[0][1]
