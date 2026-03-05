def build_transaction_features(txn, user):
    features = {}

    amount = float(txn.get("amount", 0))
    avg_amount = float(user.get("avg_amount", 1)) or 1

    hour = int(txn.get("hour", 12))
    velocity = int(txn.get("txns_last_5min", 0))

    features["amount_ratio"] = amount / avg_amount
    features["odd_hour"] = int(hour < 5 or hour > 23)

    features["new_device"] = int(txn.get("new_device", 0))
    features["new_location"] = int(txn.get("new_location", 0))
    features["velocity"] = velocity

    features["high_value_txn"] = int(amount > avg_amount * 5)

    features["behavior_deviation"] = int(
        features["amount_ratio"] > 3 or
        velocity > 3 or
        features["odd_hour"] == 1
    )

    return features