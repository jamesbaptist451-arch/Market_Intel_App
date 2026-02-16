import numpy as np
from scipy.stats import norm

class RiskManager:

    @staticmethod
    def var(returns, confidence=0.95):
        mean = np.mean(returns)
        std = np.std(returns)
        return norm.ppf(1-confidence, mean, std)

    @staticmethod
    def cvar(returns, confidence=0.95):
        var = RiskManager.var(returns, confidence)
        return np.mean([r for r in returns if r <= var])

    @staticmethod
    def kelly(win_rate, rr):
        return win_rate - ((1 - win_rate) / rr)

    @staticmethod
    def dynamic_position_size(capital, kelly_fraction, volatility):
        adj_kelly = kelly_fraction / (1 + volatility)
        return capital * adj_kelly
