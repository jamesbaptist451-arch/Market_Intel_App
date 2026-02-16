import numpy as np
from scipy.optimize import minimize

class WeightOptimizer:

    def optimize(self, feature_matrix, returns):

        def objective(weights):
            signal = np.dot(feature_matrix, weights)
            strategy_returns = signal * returns
            sharpe = np.mean(strategy_returns) / np.std(strategy_returns)
            return -sharpe

        initial = np.ones(feature_matrix.shape[1])
        bounds = [(0, 3)] * feature_matrix.shape[1]

        result = minimize(objective, initial, bounds=bounds)
        return result.x
