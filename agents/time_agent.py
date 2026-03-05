def analyze(features):
    if features["odd_hour"]:
        return {
            "risk": 0.2,
            "reason": "Transaction at an unusual time"
        }
    return {"risk": 0.0}