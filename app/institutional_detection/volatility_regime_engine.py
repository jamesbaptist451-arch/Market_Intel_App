class VolatilityRegime:

    @staticmethod
    def detect_regime(atr_series):
        mean_atr = np.mean(atr_series)
        if mean_atr > np.percentile(atr_series, 75):
            return "Expansion"
        elif mean_atr < np.percentile(atr_series, 25):
            return "Compression"
        return "Normal"
