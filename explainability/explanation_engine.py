def explain(reasons, score):
    return {
        "fraud_score": round(score, 2),
        "reasons": reasons
    }