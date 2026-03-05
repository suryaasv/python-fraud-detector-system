def decide(agent_results):
    total_risk = 0.0
    reasons = []

    for agent in agent_results:
        total_risk += agent.get("risk", 0)
        if "reason" in agent:
            reasons.append(agent["reason"])

    # Normalize risk to probability (0–1)
    fraud_probability = min(round(total_risk / 5, 2), 1.0)

    if fraud_probability >= 0.5:
        return "REJECTED", fraud_probability, reasons
    elif fraud_probability >= 0.3:
        return "APPEALABLE", fraud_probability, reasons
    else:
        return "APPROVED", fraud_probability, reasons