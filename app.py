import pandas as pd
import time
import uuid

from features.transaction_features import build_transaction_features
from agents.behavior_agent import analyze as behavior_agent
from agents.device_agent import analyze as device_agent
from agents.velocity_agent import analyze as velocity_agent
from agents.time_agent import analyze as time_agent
from agents.geo_velocity_agent import analyze as geo_velocity_agent
from agents.decision_agent import decide
from explainability.reason_formatter import format_reason
from database.db_loader import load_table
from agents.document_agent import analyze as document_agent

users = load_table("users")
txns = load_table("transactions")
kyc = load_table("kyc")

print("=== DIGITAL ACCOUNT OPENING (DAO) DOCUMENT DEFENSE ===")

for _, row in kyc.iterrows():
    start_time = time.time()

    applicant_id = row["applicant_id"]
    doc_result = document_agent(row)

    doc_risk = doc_result.get("risk", 0.0)
    latency_ms = max((time.time() - start_time) * 1000, 1.0)

    if doc_risk >= 0.7:
        dao_decision = "REJECTED"
        risk_label = "High"
    elif doc_risk >= 0.3:
        dao_decision = "REVIEW"
        risk_label = "Medium"
    else:
        dao_decision = "APPROVED"
        risk_label = "Low"

    reason = doc_result.get("reason", "Document checks passed")

    print(f"DAO Alert: Applicant-ID {applicant_id} - {dao_decision}")
    print(f"DAO Risk Score: {round(min(doc_risk, 1.0), 2)} ({risk_label})")
    print(f"Reason: {reason}")
    print(f"Time taken: {round(latency_ms, 2)} ms")
    print("------")


# =========================
# 2) Transaction Fraud Detection
# =========================
print("\n=== REAL-TIME TRANSACTION FRAUD DETECTION ===")

for _, txn in txns.iterrows():
    start_time = time.time()

    user = users[users.user_id == txn.user_id].iloc[0]
    features = build_transaction_features(txn, user)

    agent_results = [
        behavior_agent(features),
        device_agent(features),
        velocity_agent(features),
        time_agent(features),
        geo_velocity_agent(features)
    ]

    decision, score, reasons = decide(agent_results)

    latency_ms = max((time.time() - start_time) * 1000, 1.0)

    transaction_id = f"TXN_{uuid.uuid4().hex[:6]}"
    reason_text = format_reason(reasons)

    print(f"Transaction-ID {transaction_id} - {decision}")

    rounded_score = round(score, 2)
    if rounded_score >= 0.55:
        print(f"Fraud Probability: {rounded_score} (High)")
    elif rounded_score >= 0.3:
        print(f"Fraud Probability: {rounded_score} (Medium)")
    else:
        print(f"Fraud Probability: {rounded_score} (Low)")

    if reason_text:
        print(f"Reason: {reason_text}")
    else:
        print("Reason: Transaction behavior within normal limits")

    print(f"Time taken: {round(latency_ms, 2)} ms")
    print("------")