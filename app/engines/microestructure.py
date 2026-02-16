import pandas as pd
import numpy as np

class MicrostructureEngine:

    @staticmethod
    def detect_equal_highs(df, tolerance=0.001):
        highs = df['high']
        equal_highs = []
        for i in range(1, len(highs)):
            if abs(highs[i] - highs[i-1]) <= highs[i] * tolerance:
                equal_highs.append(i)
        return equal_highs

    @staticmethod
    def detect_liquidity_sweep(df):
        sweeps = []
        for i in range(2, len(df)):
            if df['high'][i] > df['high'][i-1] and df['close'][i] < df['high'][i-1]:
                sweeps.append(i)
        return sweeps

    @staticmethod
    def atr(df, period=14):
        df['tr'] = np.maximum(
            df['high'] - df['low'],
            np.maximum(
                abs(df['high'] - df['close'].shift()),
                abs(df['low'] - df['close'].shift())
            )
        )
        return df['tr'].rolling(period).mean()
