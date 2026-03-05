def analyze(kyc):
    risk = 0
    reasons = []

    if kyc["document_clear"] == 0:
        risk += 0.3
        reasons.append("Document image unclear")

    if kyc["document_valid"] == 0:
        risk += 0.4
        reasons.append("Document authenticity failed")

    if kyc["duplicate_document"] == 1:
        risk += 0.5
        reasons.append("Document already used for another account")

    if risk > 0:
        return {"risk": risk, "reason": ", ".join(reasons)}

    return {"risk": 0}