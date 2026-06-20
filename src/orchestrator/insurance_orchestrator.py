from src.agents.claim_extraction_agent import ClaimExtractionAgent
from src.agents.image_analysis_agent import ImageAnalysisAgent
from src.agents.evidence_matching_agent import EvidenceMatchingAgent
from src.agents.decision_agent import DecisionAgent

from src.services.business_rule_engine import BusinessRuleEngine
from src.services.image_quality_validator import ImageQualityValidator


class InsuranceOrchestrator:

    def __init__(self):
        self.claim_agent = ClaimExtractionAgent()
        self.image_validator = ImageQualityValidator()
        self.image_agent = ImageAnalysisAgent()
        self.matching_agent = EvidenceMatchingAgent()
        self.rule_engine = BusinessRuleEngine()
        self.decision_agent = DecisionAgent()

    def process_claim(
        self,
        conversation: str,
        image_paths: list[str],
    ):

        # --------------------------------------------------
        # STEP 1 : Validate image quality
        # --------------------------------------------------

        quality_report = self.image_validator.validate(image_paths)

        invalid_images = [
            img
            for img in quality_report
            if not img["valid"]
        ]

        if invalid_images:
            return {
                "claim": None,
                "image_quality": quality_report,
                "image_analysis": None,
                "matching": None,
                "business_rules": None,
                "decision": {
                    "status": "REJECT",
                    "reason": "One or more submitted images failed quality validation."
                }
            }

        # --------------------------------------------------
        # STEP 2 : Extract claim
        # --------------------------------------------------

        claim = self.claim_agent.extract(conversation)

        # --------------------------------------------------
        # STEP 3 : Analyze image
        # --------------------------------------------------

        image_analysis = self.image_agent.analyze(image_paths)

        # --------------------------------------------------
        # STEP 4 : Match evidence
        # --------------------------------------------------

        matching = self.matching_agent.match(
            claim,
            image_analysis,
        )

        # --------------------------------------------------
        # STEP 5 : Business Rule Engine
        # --------------------------------------------------

        rule_result = self.rule_engine.evaluate(
            claim,
            image_analysis,
            matching,
        )

        if rule_result["status"] == "REJECT":
            return {
                "claim": claim,
                "image_quality": quality_report,
                "image_analysis": image_analysis,
                "matching": matching,
                "business_rules": rule_result,
                "decision": None,
            }

        # --------------------------------------------------
        # STEP 6 : Final AI Decision
        # --------------------------------------------------

        decision = self.decision_agent.decide(
            claim,
            matching,
            rule_result
        )

        # --------------------------------------------------
        # FINAL OUTPUT
        # --------------------------------------------------

        return {
            "claim": claim,
            "image_quality": quality_report,
            "image_analysis": image_analysis,
            "matching": matching,
            "business_rules": rule_result,
            "decision": decision,
        }