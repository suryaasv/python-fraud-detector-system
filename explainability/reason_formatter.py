def format_reason(reasons):
    if not reasons:
        return "Transaction behavior within normal limits"

    # Keep it short & enterprise-style
    mapping = {
        "Amount far above user's normal spending": "abnormal spend pattern",
        "Transaction from new device and new location": "new device & location",
        "Multiple rapid transactions detected": "velocity spike"
    }

    short_reasons = [mapping.get(r, r) for r in reasons]
    return ", ".join(short_reasons)