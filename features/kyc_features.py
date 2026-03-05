def build_kyc_features(kyc_row):
    features = {}

    # Identity consistency
    features["identity_risk"] = 1 - kyc_row["face_match"]

    # Liveness risk
    features["liveness_risk"] = 1 - kyc_row["liveness"]

    # Document quality risk
    features["document_risk"] = 1 - kyc_row["id_quality"]

    return features