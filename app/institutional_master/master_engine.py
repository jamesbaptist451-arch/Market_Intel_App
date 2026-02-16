import pandas as pd
from core.liquidity_engine import LiquidityEngine
from core.absorption_engine import AbsorptionEngine
from core.delta_engine import DeltaEngine
from core.imbalance_engine import ImbalanceEngine
from core.structure_engine import StructureEngine
from core.volatility_engine import VolatilityRegime
from scoring.institutional_score import InstitutionalScore
from backtesting.backtest_engine import BacktestEngine
from ml.pattern_model import PatternModel


class InstitutionalMasterEngine:

    def __init__(self):
        self.model = PatternModel()

    def analyze(self, df, bid_vol=None, ask_vol=None):

        events = []

        # Liquidity
        sweeps = LiquidityEngine.detect_sweep(df)
        events.extend(sweeps)

        # Delta
        if bid_vol and ask_vol:
            cum_delta = DeltaEngine.cumulative_delta(bid_vol, ask_vol)
            divergences = DeltaEngine.divergence(df['close'], cum_delta)
            events.extend(divergences)

            absorption = AbsorptionEngine.detect_absorption(
                cum_delta, df['close']
            )
            events.extend(absorption)

        # Imbalance
        atr = df['high'] - df['low']
        displacement = ImbalanceEngine.detect_displacement(df, atr)
        fvg = ImbalanceEngine.detect_fvg(df)

        events.extend(displacement)
        events.extend(fvg)

        # Structure
        bos = StructureEngine.break_of_structure(df)
        events.extend(bos)

        # Regime
        regime = VolatilityRegime.detect_regime(atr)

        # Score
        score = InstitutionalScore.compute(events, regime)

        # ML Prediction
        prediction = self.model.predict(score)

        return {
            "events": events,
            "regime": regime,
            "institutional_score": score,
            "ml_prediction": prediction
        }

    def backtest(self, df):
        bt = BacktestEngine()
        return bt.run(df)
