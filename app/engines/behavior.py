class BehaviorEngine:

    @staticmethod
    def impulsive_percentage(trades):
        if not trades:
            return 0
        impulsives = len([t for t in trades if t.impulsive == 1])
        return impulsives / len(trades)

    @staticmethod
    def best_session(trades):
        session_perf = {}
        for t in trades:
            session_perf.setdefault(t.session, []).append(t.result_r)
        return {k: sum(v)/len(v) for k, v in session_perf.items()}
