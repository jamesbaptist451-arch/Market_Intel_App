import numpy as np

class StatisticsEngine:

    @staticmethod
    def win_rate(results):
        wins = len([r for r in results if r > 0])
        return wins / len(results) if results else 0

    @staticmethod
    def profit_factor(results):
        gross_profit = sum([r for r in results if r > 0])
        gross_loss = abs(sum([r for r in results if r < 0]))
        return gross_profit / gross_loss if gross_loss != 0 else 0

    @staticmethod
    def expectancy(results):
        if not results:
            return 0
        wr = StatisticsEngine.win_rate(results)
        avg_win = np.mean([r for r in results if r > 0]) if any(r > 0 for r in results) else 0
        avg_loss = abs(np.mean([r for r in results if r < 0])) if any(r < 0 for r in results) else 0
        return (wr * avg_win) - ((1 - wr) * avg_loss)

    @staticmethod
    def max_drawdown(equity_curve):
        peak = equity_curve[0]
        max_dd = 0
        for value in equity_curve:
            if value > peak:
                peak = value
            dd = (peak - value)
            max_dd = max(max_dd, dd)
        return max_dd
