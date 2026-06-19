from dataclasses import dataclass


@dataclass
class Decision:
    status: str
    risk_level: str
    fraud_score: int
    recommendation: str
    reason: str