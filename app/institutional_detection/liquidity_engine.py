import numpy as np

class LiquidityEngine:

    @staticmethod
    def detect_equal_levels(df, tolerance=0.0005):
        levels = []
        for i in range(2, len(df)):
            if abs(df['high'][i] - df['high'][i-1]) <= df['high'][i] * tolerance:
                levels.append(("equal_high", i))
            if abs(df['low'][i] - df['low'][i-1]) <= df['low'][i] * tolerance:
                levels.append(("equal_low", i))
        return levels

    @staticmethod
    def detect_sweep(df):
        sweeps = []
        for i in range(3, len(df)):
            prev_high = max(df['high'][i-3:i])
            prev_low = min(df['low'][i-3:i])

            if df['high'][i] > prev_high and df['close'][i] < prev_high:
                sweeps.append(("buy_side_liquidity_sweep", i))

            if df['low'][i] < prev_low and df['close'][i] > prev_low:
                sweeps.append(("sell_side_liquidity_sweep", i))

        return sweeps
