class BacktestEngine:

    def run(self, df):

        equity = 100000
        equity_curve = []

        for i in range(10, len(df)):
            score = df['institutional_score'][i]

            if score >= 6:
                equity *= 1.02
            elif score <= 2:
                equity *= 0.99

            equity_curve.append(equity)

        return equity_curve
