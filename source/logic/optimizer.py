import collections
import itertools
import enum
import dataclasses

from source.model.structure import Resource, Task, Pivot, Edge
from source.logic.assembling import Assembling



class Action(enum.Enum):

    build: str = enum.auto()
    unbuild: str = enum.auto()

@dataclasses.dataclass
class Tasking:

    resources: tuple[Resource]

    @property
    def resource(self):
        return sum(resource.resource for resource in self.resources)

class Optimizer:

    def __init__(self, resources: tuple[Resource], task: Task):

        self.resources = resources
        self.task = task
    
    @property
    def availabilities(self) -> tuple[Resource]:

        filtering = filter(
            lambda resource: resource.is_available,
            self.resources
        )

        return filtering
    
    @property
    def unavailabilities(self) -> tuple[Resource]:

        filtering = tuple(
            filter(
                lambda resource: not resource.is_available and resource.task.priority <= self.task.priority,
                self.resources
            )
        )

        clustering = tuple(
            Tasking(tuple(resources))
            for task, resources in itertools.groupby(
                sorted(
                    filtering,
                    key=lambda resource: resource.task.identifier
                ),
                lambda resource: resource.task.identifier
            )
        )
            
        grouping = {
            resource: sorted(
                tuple(resource.resources for resource in resources),
                key=lambda resources: len(resources)
            )
            for resource, resources in itertools.groupby(
                sorted(
                    clustering,
                    key=lambda tasking: tasking.resource
                ),
                lambda tasking: tasking.resource
            )
        }

        return grouping
    
    @property
    def assemblings(self) -> dict[Assembling]:

        assembling: tuple[Assembling] = Assembling\
            .generator(
                sorted(
                    self.availabilities,
                    key=lambda resource: resource.resource
                )
            )

        grouping = itertools.groupby(
            sorted(
                assembling,
                key=lambda assembling: assembling.resources
            ),
            lambda assembling: assembling.resources
        )

        sorting = collections.OrderedDict(
            {
                resources: tuple(sorted(assemblings,key=lambda assembling: len(assembling.indices)))
                for resources, assemblings in grouping
            }
        )

        return sorting

    @property
    def building(self) -> tuple[Assembling]:

        resources = self.assemblings.keys()
        
        resource = dict(enumerate(resources))
        edge = Edge(head=0, tail=len(resources))
        pivot = Pivot(window=len(resources))

        while pivot.head <= pivot.tail:

            if self.task.requirement == resource[pivot.middle]:
                break

            elif self.task.requirement > resource[pivot.middle]:
                pivot.head = pivot.middle + 1

            elif self.task.requirement < resource[pivot.middle]:
                pivot.tail = pivot.middle - 1
        
        if pivot.middle in edge:
            return self.assemblings[resource[pivot.middle]] 
    
    @property
    def unbuilding(self) -> tuple[Assembling]:
        return self.unavailabilities

    def optimize(self, action: Action) -> tuple[Assembling]:
        if action == Action.build:
            return self.building
        elif action == Action.unbuild:
            return self.unbuilding

