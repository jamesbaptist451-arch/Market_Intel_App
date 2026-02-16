class SpoofingDetector:

    @staticmethod
    def detect(orderbook_snapshots):

        spoof_events = []

        for i in range(1, len(orderbook_snapshots)):

            prev = orderbook_snapshots[i-1]
            curr = orderbook_snapshots[i]

            for price, size in prev['asks']:
                size_now = next((s for p, s in curr['asks'] if p == price), 0)

                if size > 1000 and size_now < size * 0.2:
                    spoof_events.append(("possible_spoof_sell", price))

        return spoof_events
