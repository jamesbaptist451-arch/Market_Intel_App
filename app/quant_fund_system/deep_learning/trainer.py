class LSTMTrainer:

    def train(self, model, X, y):

        model.fit(
            X, y,
            epochs=20,
            batch_size=64,
            validation_split=0.2
        )

        model.save("lstm_quant_model.h5")
        return model
