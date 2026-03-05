def analyze(features):
    return {
        "risk": features["amount_ratio"] > 5,
        "reason": "Amount far from normal"
    }