def analyze(features):
    if features["velocity"] > 3:
        return {
            "risk": 0.3,
            "reason": "Multiple transactions in a short time"
        }
    return {"risk": 0.0}