class DatasetBuilder:

    @staticmethod
    def build(df):
        X = df[['volatility', 'momentum', 'range', 'volume_z']]
        y = (df['returns'].shift(-1) > 0).astype(int)
        return X[:-1], y[:-1]
