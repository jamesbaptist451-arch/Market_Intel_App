import numpy as np

class GEXEngine:

    @staticmethod
    def calculate_gex(strikes, gamma, open_interest):

        gex = []

        for k, g, oi in zip(strikes, gamma, open_interest):
            exposure = g * oi * 100
            gex.append((k, exposure))

        total_gex = sum(e[1] for e in gex)

        regime = "Positive Gamma" if total_gex > 0 else "Negative Gamma"

        return {
            "total_gex": total_gex,
            "regime": regime,
            "levels": gex
        }
