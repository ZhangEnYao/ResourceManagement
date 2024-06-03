import dataclasses

@dataclasses.dataclass
class Infinity:

    positive: float = float('inf')
    neutral: int = 0
    negative: float = float('-inf')