from fastapi import APIRouter
from app.engines.statistics import StatisticsEngine
from app.services.narrative_ai import NarrativeAI

router = APIRouter()

@router.post("/analyze")
def analyze(results: list):
    wr = StatisticsEngine.win_rate(results)
    pf = StatisticsEngine.profit_factor(results)
    exp = StatisticsEngine.expectancy(results)

    narrative = NarrativeAI.generate(
        micro="Barrida confirmada",
        stats={"wr": wr, "pf": pf, "exp": exp},
        macro_bias="Alcista"
    )

    return {
        "win_rate": wr,
        "profit_factor": pf,
        "expectancy": exp,
        "narrative": narrative
    }
