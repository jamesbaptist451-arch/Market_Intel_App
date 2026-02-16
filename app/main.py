from fastapi import FastAPI
from app.database import Base, engine
from app.quant_fund_system.master_quant_engine import MasterQuantEngine
import pandas as pd
import numpy as np

Base.metadata.create_all(bind=engine)

app = FastAPI()
engine_quant = MasterQuantEngine()


@app.get("/run-quant-system")
def run_quant_system():

    # Simulación de datos reales
    df = pd.DataFrame({
        "close": np.random.rand(300) * 100,
        "volume": np.random.rand(300) * 1000
    })

    result = engine_quant.full_analysis(
        df=df,
        orderbook=[],
        options_data={
            "strikes": [],
            "gamma": [],
            "oi": []
        }
    )

    return result

