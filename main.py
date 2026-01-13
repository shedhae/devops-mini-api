from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI, Request
import logging
import time

app = FastAPI()
Instrumentator().instrument(app).expose(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

logger = logging.getLogger("devops-mini-api")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    logger.info(
        f"method={request.method} path={request.url.path} "
        f"status={response.status_code} duration={process_time:.4f}s"
    )
    
    return response

@app.get("/")
def root():
    return {"message": "DevOps Mini API"}

@app.get("/health")
def health():
    return {"status": "ok"}
