import enum
import re
import inspect
import pydantic
import dataclasses
import typing

from source.utility.data_structure import LexicographicalOrdering
from source.utility.mathematic import Infinity

class Identifier:

    class Meta(enum.Enum):
        pass

    class Normal(Meta):

        validation: int = enum.auto()
        inference: int = enum.auto()
        fine_tuning: int = enum.auto()
    
    class Special(Meta):

        urgent_task: int = Infinity.neutral
        upcoming_task: int = Infinity.neutral

class Identifiers:

    members =  {
        tuple(re.split(pattern='[^a-zA-Z]', string=key.lower())): value
        for name, identifier in inspect.getmembers(Identifier) if (inspect.isclass(identifier) and issubclass(identifier, Identifier.Meta) and identifier != Identifier.Meta)
            for key, value in identifier.__members__.items()
    }

    @classmethod
    def get(cls, name: str) -> Identifier.Meta:

        return cls.members[tuple(re.split(pattern='[^a-zA-Z]', string=name.lower()))]
    
class Orderings:

    configuration = {
        Identifier.Special.urgent_task: (Infinity.positive, Identifier.Special.urgent_task.value),
        Identifier.Special.upcoming_task: (Infinity.negative, Identifier.Special.upcoming_task.value),
        **{identifier: (Infinity.neutral, identifier.value) for identifier in Identifier.Normal}
    }
    
    @classmethod
    def get(cls, identifier: Identifier) -> LexicographicalOrdering:

        return LexicographicalOrdering(cls.configuration[identifier])
