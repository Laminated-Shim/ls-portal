from fastapi import FastAPI

from .database import init_db
from .routes.product_review import router as Router

app = FastAPI(
    title="Logic Automation LLC",
    description="Test API.",
    summary="Beta testing cody.",
    version="0.0.1",
    terms_of_service="https://github.com/logic-automation/fastAPI_react",
    contact={
        "name": "Andrew",
        "url": "https:logicautomationllc.com/#contact",
        "email": "andrew@logicautomationllc.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")

@app.on_event("startup")
async def start_db():
    await init_db()

@app.get("/", tags=["Root"])
async def read_root() -> dict:
    return {"message": "Welcome to your beanie powered app!"}
