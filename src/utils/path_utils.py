from pathlib import Path

# Root folder of the project
PROJECT_ROOT = Path(__file__).resolve().parents[2]


def resolve_image_path(image_path: str) -> Path:
    """
    Convert the image path from the CSV into the real file path.
    Example:
        images/sample/case_001/img_1.jpg
    becomes:
        <project>/dataset/images/sample/case_001/img_1.jpg
    """
    return PROJECT_ROOT / "dataset" / image_path