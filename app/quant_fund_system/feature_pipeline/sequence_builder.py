import numpy as np

class SequenceBuilder:

    @staticmethod
    def build_sequences(data, window=30):

        X, y = [], []

        for i in range(len(data) - window - 1):
            X.append(data[i:i+window])
            y.append(1 if data[i+window+1] > data[i+window] else 0)

        return np.array(X), np.array(y)
