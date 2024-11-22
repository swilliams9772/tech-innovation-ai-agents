from dataclasses import dataclass
from typing import List

@dataclass
class Task:
    name: str
    required_capabilities: List[str]
    parameters: dict
    priority: int = 1

# Example usage
analysis_task = Task(
    name="analyze_dataset",
    required_capabilities=["data_analysis"],
    parameters={
        "dataset_path": "path/to/data",
        "analysis_type": "regression"
    }
) 