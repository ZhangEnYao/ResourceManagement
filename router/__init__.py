import fastapi

from .optimization import router as router_optimization

router = fastapi.APIRouter()
router.include_router(router=router_optimization)