AI Fraud Defense System:
An AI-driven fraud prevention system that protects banks during Digital Account Opening (DAO) and real-time transactions. The system verifies onboarding documents and analyzes transaction behavior using multiple fraud detection agents to detect suspicious activities and provide explainable decisions in milliseconds.

Project Overview:
Banks process millions of digital transactions every day while onboarding new customers online. Fraudsters exploit these systems using stolen identities, synthetic identities, and abnormal transaction behavior.
This project demonstrates a multi-agent fraud detection system that:
• Verifies identity documents during account onboarding
• Monitors transaction behavior in real time
• Detects abnormal patterns such as unusual spending, device changes, and transaction spikes
• Produces explainable fraud decisions instantly

Key Features:
• Digital Account Opening (DAO) Defense
Detects suspicious documents by checking clarity, authenticity, and duplication.
• Real-Time Fraud Detection
Analyzes transaction behavior patterns to detect anomalies.
• Multi-Agent Risk Analysis
Different agents evaluate fraud signals independently.
• Explainable Decisions
The system clearly explains why a transaction or application was flagged.
• Millisecond Response Time
Fraud decisions are generated quickly to prevent financial losses.

System Workflow:
User uploads identity documents for account opening.
Documents are verified by the document verification agent.
The system approves, reviews, or rejects account creation.
Approved users perform banking transactions.
Transaction data is loaded from the MySQL database.
Behavior features are generated from transaction patterns.
Multiple fraud detection agents analyze the signals.
A decision engine combines risk scores.
The system outputs APPROVED / REVIEW / REJECTED decisions with explanations.
