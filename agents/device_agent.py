def analyze(features):
    if features["new_device"] and features["new_location"]:
        return {"risk": True, "reason": "New device + New location"}
    return {"risk": False}