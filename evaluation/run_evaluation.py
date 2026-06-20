import sys
import json
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.orchestrator.insurance_orchestrator import InsuranceOrchestrator


DATASET_DIR = Path("dataset/images/sample")


def get_cases():
    cases = []

    for case_dir in sorted(DATASET_DIR.iterdir()):

        if not case_dir.is_dir():
            continue

        images = sorted(case_dir.glob("*.jpg"))

        cases.append(
            {
                "case_id": case_dir.name,
                "images": [str(i) for i in images],
            }
        )

    return cases


def main():

    orchestrator = InsuranceOrchestrator()

    cases = get_cases()[:1]

    print(f"\nFound {len(cases)} cases\n")

    conversation = """
My car was hit from behind.
The rear bumper has a dent.
"""

    predictions = []

    total_start = time.perf_counter()

    for case in cases:

        print("=" * 60)
        print("Running:", case["case_id"])
        print("=" * 60)

        start = time.perf_counter()

        try:

            result = orchestrator.process_claim(
                conversation=conversation,
                image_paths=case["images"],
            )
            print("claim:", type(result["claim"]))
            print("image_analysis:", type(result["image_analysis"]))
            print("matching:", type(result["matching"]))
            print("decision:", type(result["decision"]))

            runtime = round(time.perf_counter() - start, 2)

            predictions.append(
                {
                    "case_id": case["case_id"],
                    "runtime_seconds": runtime,
                    "claim": result["claim"].__dict__ if result["claim"] else None,
                    "image_analysis": result["image_analysis"],
                    "matching": result["matching"],
                    "business_rules": result["business_rules"],
                    "decision": result["decision"],
                
                }
            )

        except Exception as e:

            print("FAILED:", e)

            predictions.append(
                {
                    "case_id": case["case_id"],
                    "error": str(e),
                }
            )

    total_runtime = round(time.perf_counter() - total_start, 2)

    output_dir = Path("evaluation") / "results"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "predictions.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(predictions, f, indent=4)

    print("\n========================================")
    print("Evaluation Complete")
    print("Cases:", len(cases))
    print("Runtime:", total_runtime, "seconds")
    print("Saved to:", output_file)
    print("========================================")


if __name__ == "__main__":
    main()