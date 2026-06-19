from dataclasses import dataclass

@dataclass
class Claim:
    user_id: str
    image_paths: str
    user_claim: str
    claim_object: str
    