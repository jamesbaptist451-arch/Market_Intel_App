class NarrativeAI:

    @staticmethod
    def generate(micro, stats, macro_bias):
        return f"""
        Microestructura detectada: {micro}.
        Win Rate actual: {stats['wr']:.2f}.
        Profit Factor: {stats['pf']:.2f}.
        Expectativa: {stats['exp']:.2f}R.
        Tendencia mayor: {macro_bias}.
        Conclusión: Setup con {'ventaja estadística' if stats['exp'] > 0 else 'riesgo estructural'}.
        """
