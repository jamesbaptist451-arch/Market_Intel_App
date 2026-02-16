from data.feature_engineering import FeatureEngineering
from ml.dataset_builder import DatasetBuilder
from ml.train_model import InstitutionalML
from optimization.weight_optimizer import WeightOptimizer
from backtesting.advanced_backtester import AdvancedBacktester

class UltraInstitutionalEngine:

    def full_pipeline(self, df):

        df = FeatureEngineering.build_features(df)
        X, y = DatasetBuilder.build(df)

        model = InstitutionalML()
        model.train(X, y)

        optimizer = WeightOptimizer()
        weights = optimizer.optimize(X.values, df['returns'].values)

        signals = X.values @ weights
        bt = AdvancedBacktester()
        equity = bt.run(signals, df['returns'].values)

        return {
            "optimized_weights": weights.tolist(),
            "final_equity": equity[-1],
            "equity_curve": equity
        }
