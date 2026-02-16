class DeltaEngine:

    @staticmethod
    def cumulative_delta(bid_vol, ask_vol):
        return np.cumsum(np.array(ask_vol) - np.array(bid_vol))

    @staticmethod
    def divergence(price, cum_delta):
        signals = []
        for i in range(2, len(price)):
            if price[i] > price[i-1] and cum_delta[i] < cum_delta[i-1]:
                signals.append(("bearish_divergence", i))
            if price[i] < price[i-1] and cum_delta[i] > cum_delta[i-1]:
                signals.append(("bullish_divergence", i))
        return signals
