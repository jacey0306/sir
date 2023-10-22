from dataclasses import dataclass

@dataclass
class SIRRequest:
    city: list[str]
    days_contagious: int = 2
    random_seed: int = 20231022
    num_trials: int = 1
    vaccine_effectiveness: float = 1
