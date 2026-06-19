from dataclasses import dataclass


@dataclass
class ExtractedClaim:
    object_type: str
    claimed_issue: str
    claimed_part: str
    claim_summary: str