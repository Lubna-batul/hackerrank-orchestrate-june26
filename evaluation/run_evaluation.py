import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pathlib import Path

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

    import json
    import time

    orchestrator = InsuranceOrchestrator()

    cases = get_cases()

    print(f"\nFound {len(cases)} cases\n")

    case = cases[0]

    print("=" * 60)
    print("Running:", case["case_id"])
    print("=" * 60)

    conversation = """
My car was hit from behind.
The rear bumper has a dent.
"""

    start = time.perf_counter()

    result = orchestrator.process_claim(
        conversation=conversation,
        image_paths=case["images"],
    )

    runtime = round(time.perf_counter() - start, 2)

    prediction = {
        "case_id": case["case_id"],
        "runtime_seconds": runtime,
        "claim": result["claim"].__dict__,
        "image_analysis": result["image_analysis"],
        "matching": result["matching"],
        "decision": result["decision"].__dict__,
    }

    output_dir = Path("evaluation") / "results"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "predictions.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(prediction, f, indent=4)

    print("\nPrediction saved to:")
    print(output_file)
if __name__ == "__main__":
    main()