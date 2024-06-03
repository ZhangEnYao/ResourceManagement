import dataclasses

import fastapi
import pydantic

from source import Resource, Task, Optimizer, Action, Identifiers, Orderings

router = fastapi.APIRouter()

@dataclasses.dataclass
class Body:

    resources: list[Resource]
    task: Task

@dataclasses.dataclass
class Parameters:
    action: Action

@router.post('/{action}')
async def build(action: str, body: Body):

    body = Body(
        resources=tuple(body.resources),
        task=body.task
    )

    parameters = Parameters(
        action=Action[action]
    )

    optimization = Optimizer(resources=body.resources, task=body.task)\
        .optimize(action=parameters.action)

    if optimization:
        response = list(
            list(
                index.identifier
                for index in assembling.indices
            )
            for assembling in optimization
        )
            
        return response