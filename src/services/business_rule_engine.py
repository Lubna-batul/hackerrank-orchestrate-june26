class BusinessRuleEngine:

    def evaluate(self, claim, image_analysis, matching):

        reasons = []

        # Rule 1: Invalid image
        if not image_analysis.get("valid_image", False):
            reasons.append("Invalid or unusable image.")
            return {
                "status": "REJECT",
                "reason": reasons,
            }

        # Rule 2: Matching confidence too low
        if matching["confidence"] < 0.50:
            reasons.append("Evidence confidence below minimum threshold.")
            return {
                "status": "REJECT",
                "reason": reasons,
            }

        # Rule 3: Medium confidence
        if matching["confidence"] < 0.80:
            reasons.append("Manual review required.")
            return {
                "status": "REVIEW",
                "reason": reasons,
            }

        # Rule 4: Risk flags detected
        if image_analysis.get("risk_flags"):
            reasons.append("Risk flags detected.")
            return {
                "status": "REVIEW",
                "reason": reasons,
            }

        return {
            "status": "PASS",
            "reason": ["Business rules passed."],
        }