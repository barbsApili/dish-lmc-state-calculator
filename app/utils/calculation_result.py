from dataclasses import dataclass


@dataclass
class CalculationResult:
    result: str
    matched_rule: str
    description: str