import pandas as pd
import numpy as np

class FeatureEngineering:

    @staticmethod
    def build_features(df):

        df['returns'] = df['close'].pct_change()
        df['volatility'] = df['returns'].rolling(20).std()
        df['momentum'] = df['close'] - df['close'].shift(10)
        df['range'] = df['high'] - df['low']
        df['volume_z'] = (df['volume'] - df['volume'].rolling(20).mean()) / df['volume'].rolling(20).std()

        df = df.dropna()
        return df
