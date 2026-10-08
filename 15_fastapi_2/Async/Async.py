import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class TaskRequest(BaseModel):
    tasks: list[str]


async def process_task(task: str) -> str:
    await asyncio.sleep(1)  # simulate async work
    return f"processed: {task}"


@app.post("/tasks/process")
def process_tasks(request: TaskRequest):
    if not request.tasks:
        raise HTTPException(
            status_code=400,
            detail="Task list cannot be empty",
        )

    results = await asyncio.gather(
        *(process_task(task) for task in request.tasks)
    )

    return {"results": results}