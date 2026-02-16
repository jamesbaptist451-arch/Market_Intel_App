
---

# 🔷 CÓMO DEBE VERSE ESE MASTER ENGINE REAL

No debe contener lógica pesada.  
Solo coordinar.

Ejemplo limpio y correcto:

```python
# app/quant_fund_system/master_engine.py

from institutional_detection.liquidity_engine import LiquidityEngine
from ultra_institutional.ml.inference import MLInference
from regime_engine.hmm_regime import HMMRegime
from risk_engine.risk_manager import RiskManager
from execution_engine.smart_execution import SmartExecution


class MasterEngine:

    def __init__(self):
        self.ml = MLInference()
        self.regime = HMMRegime()
        self.risk = RiskManager()
        self.execution = SmartExecution()

    def run(self, market_data, capital):

        # 1️⃣ Institutional detection
        inst_score = LiquidityEngine.detect_sweep(market_data["df"])

        # 2️⃣ ML probability
        dl_prob = self.ml.predict(market_data["features"])

        # 3️⃣ Regime detection
        self.regime.train(market_data["returns"])
        regime_state = self.regime.detect(market_data["returns"])

        # 4️⃣ Signal fusion
        signal = (0.6 * dl_prob) + (0.4 * len(inst_score))

        # 5️⃣ Risk control
        position = self.risk.dynamic_position_size(
            capital=capital,
            kelly_fraction=0.02,
            volatility=market_data["volatility"]
        )

        # 6️⃣ Execution
        execution = self.execution.simulate_execution(
            signal,
            market_data["price"],
            market_data["volume"],
            market_data["depth"]
        )

        return {
            "signal": signal,
            "position_size": position,
            "execution": execution,
            "regime_state": regime_state.tolist()
        }
