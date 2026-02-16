import numpy as np

class OrderBookHeatmap:

    @staticmethod
    def build(orderbook):

        prices = []
        sizes = []

        for bid in orderbook['bids']:
            prices.append(float(bid[0]))
            sizes.append(float(bid[1]))

        for ask in orderbook['asks']:
            prices.append(float(ask[0]))
            sizes.append(float(ask[1]))

        intensity = np.log1p(sizes)

        return {
            "prices": prices,
            "intensity": intensity.tolist()
        }
