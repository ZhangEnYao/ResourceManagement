import dataclasses
import math

from source.utility.data_structure import LexicographicalOrdering
from source.logic.task import Identifiers, Orderings

@dataclasses.dataclass(unsafe_hash=True)
class Task:

    identifier: str
    task: str
    requirement: int = None

    def __post_init__(self):

        self.task = Identifiers.get(self.task)
    
    @property
    def priority(self):

        return Orderings.get(self.task)

@dataclasses.dataclass
class Resource:

    identifier: str
    resource: int
    is_available: bool
    task: Task = None

@dataclasses.dataclass(unsafe_hash=True)
class Window:

    head: int
    tail: int

@dataclasses.dataclass(unsafe_hash=True)
class Pivot:

    window: int
    
    def __post_init__(self):

        self.head = 0
        self.tail = self.head + self.window - 1

    @property
    def middle(self):
        return math.ceil((self.head + self.tail)/2)

@dataclasses.dataclass
class Edge:

    head: int
    tail: int

    def __contains__(self, element: int):
        return self.head <= element < self.tail
    