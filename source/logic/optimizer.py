import math
import itertools
import dataclasses
import typing


from source.model.structure import Resource, Task, Tasking, Action, Request
from source.logic.collection import Assemblage, Combination

class Searcher:

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
    
    @classmethod
    def search(cls, object: object, pool: dict):

        resources = pool.keys()
        
        resource = dict(enumerate(resources))
        edge = Searcher.Edge(head=0, tail=len(resources))
        pivot = Searcher.Pivot(window=len(resources))

        while pivot.head <= pivot.tail:

            if object == resource[pivot.middle]:
                break

            elif object > resource[pivot.middle]:
                pivot.head = pivot.middle + 1

            elif object < resource[pivot.middle]:
                pivot.tail = pivot.middle - 1
        
        if pivot.middle in edge:
            return pool[resource[pivot.middle]] 

class Optimizer:

    def __init__(self, resources: tuple[Resource], task: Task):

        self.resources = resources
        self.task = task
    
    @property
    def unbuilding(self) -> tuple[Combination]:

        releaseabilities = tuple(
            filter(
                lambda resource: not resource.is_available and resource.tasking.priority <= self.task.priority,
                self.resources
            )
        )
        availibilities = tuple(
            resource
            for resource in self.resources
            if resource.is_available
        )

        request = Request(
            requirement=self.task.requirement - sum(resource.resource for resource in availibilities),
            unit=int(math.pow(2, math.floor(math.log2(len(availibilities))) + 1)) - len(availibilities),
        )

        taskings = tuple(
            Tasking(
                identifier=task,
                resources=tuple(resources)
            )
            for task, resources in itertools.groupby(
                sorted(
                    releaseabilities,
                    key=lambda resource: resource.tasking.identifier
                ),
                lambda resource: resource.tasking.identifier
            )
        )

        combinations = tuple(
            Combination.generator(
                taskings=sorted(
                    taskings,
                    key=lambda resource: resource.resource
                )
            )
        )

        combinations = {
            resource: tuple(
                sorted(
                    tuple(subcombination for subcombination in subcombinations if not subcombination.unit < request.unit),
                    key=lambda subcombination: subcombination.unit
                )
            )
            for resource, subcombinations in itertools.groupby(
                sorted(
                    combinations,
                    key=lambda combination: combination.resource
                ),
                lambda combination: combination.resource
            )
        }

        supremum = Searcher.search(
            object=request.requirement,
            pool=combinations,
        )

        return supremum
    
    @property
    def building(self) -> dict[Assemblage]:
        
        availabilities = tuple(
            filter(
                lambda resource: resource.is_available,
                self.resources
            )
        )

        assemblings: tuple[Assemblage] = tuple(
            Assemblage.generator(
                resources=sorted(
                    availabilities,
                    key=lambda resource: resource.resource
                )
            )
        )

        assemblings = {
            resource: tuple(
                sorted(
                    subassemblings,
                    key=lambda subassembling: subassembling.unit
                )
            )
            for resource, subassemblings in itertools.groupby(
                sorted(
                    assemblings,
                    key=lambda assembling: assembling.resource
                ),
                lambda assembling: assembling.resource
            )
        }

        supremum = Searcher.search(
            object=self.task.requirement,
            pool=assemblings,
        )

        return supremum

    def optimize(self, action: Action) -> tuple[typing.Union[Assemblage, Combination]]:

        if action == Action.build:
            return self.building
        
        elif action == Action.unbuild:
            return self.unbuilding
    
    @classmethod
    def transformer(cls, optimization: tuple[typing.Union[Assemblage, Combination]]):

        if optimization:

            response = list(
                list(
                    index.identifier
                    for index in collection.resources
                )
                for collection in optimization
            )
                
            return response

        return None
        