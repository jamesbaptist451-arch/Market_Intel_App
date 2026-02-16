import numpy as np

class WalkForwardEngine:

    def run(self, model_class, X, y, train_size=0.6, step=100):

        n = len(X)
        train_end = int(n * train_size)

        results = []

        while train_end + step < n:

            X_train = X[:train_end]
            y_train = y[:train_end]

            X_test = X[train_end:train_end+step]
            y_test = y[train_end:train_end+step]

            model = model_class()
            model.train(X_train, y_train)

            preds = model.model.predict(X_test)
            acc = np.mean((preds.flatten() > 0.5) == y_test)

            results.append(acc)

            train_end += step

        return {
            "fold_accuracies": results,
            "mean_accuracy": np.mean(results)
        }
