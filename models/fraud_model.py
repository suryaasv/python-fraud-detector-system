def fraud_probability(features):
    score = 0

    if features["amount_ratio"] > 5:
        score += 0.4
    if features["velocity"] > 3:
        score += 0.3
    if features["odd_hour"]:
        score += 0.2
    if features["new_device"] and features["new_location"]:
        score += 0.2

    return min(score, 1.0)