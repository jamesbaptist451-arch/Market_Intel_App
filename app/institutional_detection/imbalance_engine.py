class ImbalanceEngine:

    @staticmethod
    def detect_displacement(df, atr):
        displacements = []
        for i in range(1, len(df)):
            body = abs(df['close'][i] - df['open'][i])
            if body > atr[i] * 1.5:
                displacements.append(("strong_displacement", i))
        return displacements

    @staticmethod
    def detect_fvg(df):
        fvg = []
        for i in range(2, len(df)):
            if df['low'][i] > df['high'][i-2]:
                fvg.append(("bullish_fvg", i))
            if df['high'][i] < df['low'][i-2]:
                fvg.append(("bearish_fvg", i))
        return fvg
