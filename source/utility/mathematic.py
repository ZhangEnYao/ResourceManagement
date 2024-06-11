import dataclasses

@dataclasses.dataclass
class Limit:

    positive: float = float('inf')
    neutral: int = 0
    negative: float = float('-inf')