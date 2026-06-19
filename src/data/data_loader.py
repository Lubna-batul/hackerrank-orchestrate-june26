from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Responsible for loading all CSV datasets used by the application.
    """

    def __init__(self, dataset_path: str = "dataset"):
        self.dataset_path = Path(dataset_path)

    def load_sample_claims(self):
        return pd.read_csv(self.dataset_path / "sample_claims.csv")

    def load_claims(self):
        return pd.read_csv(self.dataset_path / "claims.csv")

    def load_user_history(self):
        return pd.read_csv(self.dataset_path / "user_history.csv")

    def load_evidence_requirements(self):
        return pd.read_csv(self.dataset_path / "evidence_requirements.csv")