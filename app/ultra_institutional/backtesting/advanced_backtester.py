import numpy as np

class AdvancedBacktester:

    def run(self, signals, returns, capital=100000):

        equity = capital
        equity_curve = [equity]

        for s, r in zip(signals, returns):
            equity *= (1 + s * r)
            equity_curve.append(equity)

        return equity_curve
