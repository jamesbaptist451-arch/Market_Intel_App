class AbsorptionEngine:

    @staticmethod
    def detect_absorption(delta, price):
        absorption = []
        for i in range(1, len(delta)):
            # delta negativo pero precio no cae
            if delta[i] < 0 and price[i] >= price[i-1]:
                absorption.append(("buy_absorption", i))

            # delta positivo pero precio no sube
            if delta[i] > 0 and price[i] <= price[i-1]:
                absorption.append(("sell_absorption", i))

        return absorption
