from app.quant_fund_system.deep_learning.lstm_model import LSTMPredictor
from app.institutional_detection.spoofing_detector import SpoofingDetector
from app.ultra_institutional.gex_engine import GEXEngine


class MasterQuantEngine:

    def __init__(self):
        self.lstm = LSTMPredictor()

    def full_analysis(self, df, orderbook, options_data):

        sequence = df['close'].values[-30:]
        dl_prob = self.lstm.predict(sequence)

        spoof = SpoofingDetector.detect(orderbook)

        gex = GEXEngine.calculate_gex(
            options_data['strikes'],
            options_data['gamma'],
            options_data['oi']
        )

        return {
            "deep_learning_prob": dl_prob,
            "spoofing_events": spoof,
            "gex_regime": gex['regime'],
            "total_gex": gex['total_gex']
        }
