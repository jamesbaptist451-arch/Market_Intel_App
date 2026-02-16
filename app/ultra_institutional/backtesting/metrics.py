import numpy as np

class HedgeMetrics:

    @staticmethod
    def sharpe(returns):
        return np.mean(returns) / np.std(returns)

    @staticmethod
    def sortino(returns):
        downside = [r for r in returns if r < 0]
        return np.mean(returns) / np.std(downside)

    @staticmethod
    def max_drawdown(equity):
        peak = equity[0]
        max_dd = 0
        for v in equity:
            peak = max(peak, v)
            max_dd = max(max_dd, peak - v)
        return max_dd

    @staticmethod
    def calmar(returns, equity):
        annual_return = np.mean(returns) * 252
        max_dd = HedgeMetrics.max_drawdown(equity)
        return annual_return / max_dd
