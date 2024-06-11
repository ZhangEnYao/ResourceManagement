import dataclasses
import math
import enum

from source.utility.data_structure import LexicographicalOrdering
from source.model.task import Identifiers, Orderings

@dataclasses.dataclass(unsafe_hash=True)
class Task:

    task: str
    identifier: str = None
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
    tasking: Task = None

@dataclasses.dataclass
class Tasking:

    identifier: str
    resources: tuple[Resource]

    @property
    def unit(self):
        return len(self.resources)
    
    @property
    def resource(self):
        return sum(resource.resource for resource in self.resources)
    
class Action(enum.Enum):

    build: str = enum.auto()
    unbuild: str = enum.auto()
    
@dataclasses.dataclass
class Request:
    unit: int
    requirement: float