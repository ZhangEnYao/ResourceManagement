import unittest

from source.logic.optimizer import Optimizer
from source.model import Action, Resource, Task

import abc as abstract_base_classes

import enum
import typing
import dataclasses

@dataclasses.dataclass
class TetstCase:

    resource: list[dict]
    task: dict
    assertion: list[list[str]]

class Configurations(abstract_base_classes.ABC):

    action: Action

    @classmethod
    @abstract_base_classes.abstractmethod
    def get_testcases(cls) -> tuple[TetstCase]:
        return NotImplemented

class Build(Configurations):

    class Scenario(enum.Enum):

        monoresource: int = enum.auto()
        biresource: int = enum.auto()
        triresource: int = enum.auto()
        equivalent_resource: int = enum.auto()

    class Resources:

        first=Resource(
            identifier="1",
            resource=23,
            is_available=True
        )

        second=Resource(
            identifier="2",
            resource=13,
            is_available=True
        )

        third=Resource(
            identifier="3",
            resource=15,
            is_available=True
        )

        fourth=Resource(
            identifier="4",
            resource=23,
            is_available=True
        )

    action = Action.build

    @classmethod
    def get_testcases(cls, scenario: Scenario) -> tuple[TetstCase]:

        if scenario == cls.Scenario.monoresource:
            return (
                TetstCase(
                    resource=(cls.Resources.first,),
                    task=Task(task="upcoming_task", requirement=22),
                    assertion=[['1']]
                ),
                TetstCase(
                    resource=(cls.Resources.first,),
                    task=Task(task="upcoming_task", requirement=23),
                    assertion=[['1']]
                ),
                TetstCase(
                    resource=(cls.Resources.first,),
                    task=Task(task="upcoming_task", requirement=24),
                    assertion=None
                ),
            )
        
        elif scenario == cls.Scenario.biresource:
            return (
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=12),
                    assertion=[["2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=13),
                    assertion=[["2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=18),
                    assertion=[["1"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=23),
                    assertion=[["1"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=24.5),
                    assertion=[["1", "2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=26),
                    assertion=[["1", "2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second),
                    task=Task(task="upcoming_task", requirement=27),
                    assertion=None
                ),
            )
        
        elif scenario == cls.Scenario.triresource:
            return (
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=12),
                    assertion=[["2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=13),
                    assertion=[["2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=14),
                    assertion=[["3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=15),
                    assertion=[["3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=19),
                    assertion=[["1"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=23),
                    assertion=[["1"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=24.5),
                    assertion=[["2", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=26),
                    assertion=[["2", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=28),
                    assertion=[["1", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=30),
                    assertion=[["1", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third),
                    task=Task(task="upcoming_task", requirement=31),
                    assertion=None
                ),
            )
        
        elif scenario == cls.Scenario.equivalent_resource:
            return (
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.fourth),
                    task=Task(task="upcoming_task", requirement=22),
                    assertion=[["1"], ["4"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.fourth),
                    task=Task(task="upcoming_task", requirement=23),
                    assertion=[["1"], ["4"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.fourth),
                    task=Task(task="upcoming_task", requirement=34.5),
                    assertion=[["1", "4"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.fourth),
                    task=Task(task="upcoming_task", requirement=46),
                    assertion=[["1", "4"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.fourth),
                    task=Task(task="upcoming_task", requirement=47),
                    assertion=None
                ),
            )
    
class Unbuild(Configurations):

    class Scenario(enum.Enum):

        priority: int = enum.auto()
        requirement: int = enum.auto()

    class Resources:

        first=Resource(
            identifier="1",
            resource=23,
            is_available=False,
            tasking=Task(
                identifier="1",
                task="fine_tuning"
            )
        )

        second=Resource(
            identifier="2",
            resource=13,
            is_available=False,
            tasking=Task(
                identifier="1",
                task="fine_tuning"
            )
        )

        third=Resource(
            identifier="3",
            resource=15,
            is_available=False,
            tasking=Task(
                identifier="2",
                task="inference"
            )
        )

        fourth=Resource(
            identifier="4",
            resource=23,
            is_available=True
        )

        fifth=Resource(
            identifier="5",
            resource=13,
            is_available=False,
            tasking=Task(
                identifier="3",
                task="reserved_task"
            )
        )
    
    action = Action.unbuild

    @classmethod
    def get_testcases(cls, scenario: Scenario) -> tuple[TetstCase]:
        if scenario == cls.Scenario.priority:
            return (
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="upcoming_task", requirement=(1)),
                    assertion=None
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="inference", requirement=(23+15)),
                    assertion=[["3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="inference", requirement=(23+16)),
                    assertion=None
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="validation", requirement=(23+15)),
                    assertion=[["3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="validation", requirement=(23+16)),
                    assertion=None
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="fine_tuning", requirement=(23+39)),
                    assertion=[["1", "2", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="fine_tuning", requirement=(23+40)),
                    assertion=None
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="urgent_task", requirement=(23+39)),
                    assertion=[["1", "2", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="urgent_task", requirement=(23+40)),
                    assertion=None
                ),
            )

        elif scenario == cls.Scenario.requirement:
            return (
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+14)),
                    assertion=[["3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+15)),
                    assertion=[["3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+20.5)),
                    assertion=[["1", "2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+26)),
                    assertion=[["1", "2"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+32.5)),
                    assertion=[["1", "2", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+39)),
                    assertion=[["1", "2", "3"]]
                ),
                TetstCase(
                    resource=(cls.Resources.first, cls.Resources.second, cls.Resources.third, cls.Resources.fourth, cls.Resources.fifth),
                    task=Task(task="model_benchmark", requirement=(23+40)),
                    assertion=None
                ),
            )

class Test(unittest.TestCase):

    def template_optimizer(self, configuration: typing.Union[Build, Unbuild], scenario: typing.Union[Build.Scenario, Unbuild.Scenario]):

        for testcase in configuration.get_testcases(scenario=scenario):

            with self.subTest(testcase=testcase):

                optimization = Optimizer(resources=testcase.resource, task=testcase.task).optimize(action=configuration.action)

                optimization = Optimizer.transformer(optimization=optimization)

                self.assertEqual(
                    tuple(set(instance) for instance in optimization) if optimization else optimization,
                    tuple(set(instance) for instance in testcase.assertion) if testcase.assertion else testcase.assertion,
                )

    def test_build_monoresource(self):
        self.template_optimizer(configuration=Build, scenario=Build.Scenario.monoresource)
    
    def test_build_biresource(self):
        self.template_optimizer(configuration=Build, scenario=Build.Scenario.biresource)
    
    def test_build_triresource(self):
        self.template_optimizer(configuration=Build, scenario=Build.Scenario.triresource)
    
    def test_build_equivalent_resource(self):
        self.template_optimizer(configuration=Build, scenario=Build.Scenario.equivalent_resource)
    
    def test_unbuild_priority(self):
        self.template_optimizer(configuration=Unbuild, scenario=Unbuild.Scenario.priority)
    
    def test_unbuild_requirement(self):
        self.template_optimizer(configuration=Unbuild, scenario=Unbuild.Scenario.requirement)

if __name__ == "__main__":
    unittest.main()