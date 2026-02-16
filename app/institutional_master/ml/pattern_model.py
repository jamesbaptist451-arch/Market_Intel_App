import numpy as np

class PatternModel:

    def predict(self, score):

        if score >= 7:
            return "High Probability Institutional Activity"
        elif score >= 4:
            return "Moderate Institutional Presence"
        else:
            return "Low Institutional Footprint"
