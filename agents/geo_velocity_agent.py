def analyze(features):
    if features["new_location"] and features["velocity"] > 2:
        return {
            "risk": 0.25,
            "reason": "Unusual location"
        }
    return {"risk": 0.0}