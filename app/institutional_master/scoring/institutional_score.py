class InstitutionalScore:

    @staticmethod
    def compute(events, regime):

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

        score = sum(weights.get(e[0], 0) for e in events)

        if regime == "Expansion":
            score *= 1.2
        elif regime == "Compression":
            score *= 0.8

        return round(score, 2)
