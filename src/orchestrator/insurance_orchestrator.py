from src.agents.claim_extraction_agent import ClaimExtractionAgent
from src.agents.image_analysis_agent import ImageAnalysisAgent
from src.agents.evidence_matching_agent import EvidenceMatchingAgent


class InsuranceOrchestrator:

    def __init__(self):
        self.claim_agent = ClaimExtractionAgent()
        self.image_agent = ImageAnalysisAgent()
        self.matching_agent = EvidenceMatchingAgent()

    def process_claim(self, conversation: str, image_paths: list[str]):

        # Step 1: Extract claim
        claim = self.claim_agent.extract(conversation)

        # Step 2: Analyze images
        image_analysis = self.image_agent.analyze(image_paths)

        # Step 3: Match evidence
        decision = self.matching_agent.match(
            claim,
            image_analysis,
        )

        return {
            "claim": claim,
            "image_analysis": image_analysis,
            "decision": decision,
        }