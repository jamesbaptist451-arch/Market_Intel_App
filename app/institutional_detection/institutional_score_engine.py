class InstitutionalScoreEngine:

    @staticmethod
    def compute_score(events):
        weights = {
            "buy_side_liquidity_sweep": 2,
            "sell_side_liquidity_sweep": 2,
            "buy_absorption": 2,
            "sell_absorption": 2,
            "bullish_divergence": 1.5,
            "bearish_divergence": 1.5,
            "strong_displacement": 2,
            "bullish_fvg": 1,
            "bearish_fvg": 1,
            "bullish_bos": 1.5,
            "bearish_bos": 1.5
        }

        score = 0
        for event, _ in events:
            score += weights.get(event, 0)

        return score
