import collections
import math
import typing_extensions

from source.model.structure import *

class Assembling:

    def __init__(self, resources: int, indices: tuple[Resource]):
        self.resources = resources
        self.indices = indices

    @classmethod
    def generator(cls, resources: tuple[Resource]) -> typing_extensions.Self:

        units = len(resources)

        if units <= 0:
            return None
        
        for power in range(math.floor(math.log(units, 2)) + 1):
            cluster_size = int(math.pow(2, power))

            for index in range(units - cluster_size + 1):

                window = Window(index, index + cluster_size)
                resource = resources[slice(window.head, window.tail)]

                yield Assembling(
                    sum(conponent.resource for conponent in resource),
                    resource,
                )

class Assemblings:

    def __init__(self, assemblings: collections.OrderedDict):
        self.assemblings = assemblings

    @property
    def size(self):
        return len(self.assemblings.keys())
    