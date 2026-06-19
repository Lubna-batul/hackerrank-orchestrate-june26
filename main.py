from src.orchestrator.insurance_orchestrator import InsuranceOrchestrator


conversation = (
    "Customer: My rear bumper has a dent after someone hit my parked car."
)

image_paths = [
    "dataset/images/sample/case_001/img_1.jpg"
]


orchestrator = InsuranceOrchestrator()

result = orchestrator.process_claim(
    conversation,
    image_paths,
)

print("\n========== FINAL PIPELINE RESULT ==========")
print(result)