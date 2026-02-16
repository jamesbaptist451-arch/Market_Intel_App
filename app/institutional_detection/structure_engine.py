class StructureEngine:

    @staticmethod
    def break_of_structure(df):
        bos = []
        for i in range(2, len(df)):
            if df['high'][i] > df['high'][i-1]:
                bos.append(("bullish_bos", i))
            if df['low'][i] < df['low'][i-1]:
                bos.append(("bearish_bos", i))
        return bos
