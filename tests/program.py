import itertools

from source import Resource, Task, Optimizer

counter = itertools.count()

if __name__ == '__main__':

    resources = (
        Resource(
            identifier=next(counter),
            resource=13,
            is_available=False
        ),
        Resource(
            identifier=next(counter),
            resource=23,
            is_available=False
        ),
        Resource(
            identifier=next(counter),
            resource=36,
            is_available=False
        ),
        Resource(
            identifier=next(counter),
            resource=10,
            is_available=True
        ),
        Resource(
            identifier=next(counter),
            resource=299,
            is_available=False
        ),
        Resource(
            identifier=next(counter),
            resource=2,
            is_available=True
        ),
    )

    tasks = (
        Task(
            task='inference',
            requirement=1,
        ),
        Task(
            task='validation',
            requirement=7,
        ),
        Task(
            task='fine_tuning',
            requirement=14,
        ),
        Task(
            task='fine_tuning',
            requirement=19,
        ),
        Task(
            task='fine_tuning',
            requirement=29,
        ),
        Task(
            task='fine_tuning',
            requirement=47,
        ),
        Task(
            task='fine_tuning',
            requirement=66,
        ),
        Task(
            task='fine_tuning',
            requirement=186,
        ),
        Task(
            task='fine_tuning',
            requirement=317,
        ),
        Task(
            task='fine_tuning',
            requirement=353,
        ),
        Task(
            task='fine_tuning',
            requirement=372,
        ),
    )

    for task in tasks:
        print(
            Optimizer(resources=resources)\
                .optimize(task=task)
        )