import math
import dataclasses

from source.model.structure import *

@dataclasses.dataclass(unsafe_hash=True)
class Window:

    head: int
    tail: int

class Assemblage:

    def __init__(self, resources: tuple[Resource]):

        self.resources = resources
    
    @property
    def unit(self):
        return len(self.resources)
    
    @property
    def resource(self):
        return min(resource.resource for resource in self.resources) * self.unit

    @classmethod
    def generator(cls, resources: tuple[Resource]):

        unit = len(resources)

        if unit <= 0:
            return None
        
        supremum = math.floor(math.log2(unit))
        for power in range(supremum + 1):

            exponent = int(math.pow(2, power))
            for index in range(unit - exponent + 1):

                window = Window(index, index + exponent)
                subresources = resources[slice(window.head, window.tail)]

                yield Assemblage(resources=subresources)

class Combination:

    def __init__(self, taskings: tuple[Tasking]):

        self.taskings = taskings
    
    @property
    def unit(self):
        return len(self.resources)
    
    @property
    def resources(self):
         return tuple(resource for tasking in self.taskings for resource in tasking.resources)
    
    @property
    def resource(self):
        return min(resource.resource for resource in self.resources) * self.unit

    @classmethod
    def generator(cls, taskings: tuple[Tasking]):

        amount = len(taskings)

        if amount <= 0:
            return None
        
        for index in range(amount):

            for span in range(1, amount-index+1):

                window = Window(index, index+span)
                subtaskings = taskings[slice(window.head, window.tail)]

                yield Combination(taskings=subtaskings)
    