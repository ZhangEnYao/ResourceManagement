import enum
import re
import inspect

from source.utility.data_structure import LexicographicalOrdering
from source.utility.mathematic import Limit

class Identifier:

    class Meta(enum.Enum):
        pass

    class Normal(Meta):

        inference: int = enum.auto()
        validation: int = enum.auto()
        fine_tuning: int = enum.auto()
        model_benchmark: int = enum.auto()
    
    class Special(Meta):

        reserved_task: int = enum.auto()
        urgent_task: int = enum.auto()
        upcoming_task: int = enum.auto()

class Identifiers:

    members =  {
        tuple(re.split(pattern='[^a-zA-Z]', string=key.lower())): value
        for name, identifier in inspect.getmembers(Identifier) if (inspect.isclass(identifier) and issubclass(identifier, Identifier.Meta) and identifier != Identifier.Meta)
            for key, value in identifier.__members__.items()
    }

    @classmethod
    def get(cls, name: str) -> Identifier.Meta:

        return cls.members[tuple(re.split(pattern='[^a-zA-Z]', string=name.lower()))]

    configuration = {
        Identifier.Special.reserved_task: (
            Limit.positive, Limit.positive
        ),
        Identifier.Special.urgent_task: (
            Limit.positive, Limit.neutral
        ),
        Identifier.Special.upcoming_task: (
            Limit.negative, Limit.neutral
        ),
        Identifier.Normal.inference: (
            Limit.neutral, 1
        ),
        Identifier.Normal.validation: (
            Limit.neutral, 2
        ),
        Identifier.Normal.fine_tuning: (
            Limit.neutral, 3
        ),
        Identifier.Normal.model_benchmark: (
            Limit.neutral, 3
        ),
    }
    
class Orderings:
    
    @classmethod
    def get(cls, identifier: Identifier) -> LexicographicalOrdering:

        return LexicographicalOrdering(Identifiers.configuration[identifier])
