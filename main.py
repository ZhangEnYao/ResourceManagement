import fastapi
import uvicorn

from router import router

application = fastapi.FastAPI()
application.include_router(router)


if __name__ == '__main__':
    uvicorn.run(
        app='__main__:application',
        reload=True
    )