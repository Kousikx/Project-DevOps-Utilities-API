from fastapi import FastAPI #impoting fast api 
from routers import metrics, aws


app = FastAPI(
    title="Internal DevOps Utilities API",
    description="API for various internal DevOps utilities",
    vesrion="1.0.0",
    doc_url="/docs",
    redoc_url="/redoc"
) #creating an instance of FastAPI

@app.get("/")
def hello():
    return {"message": "Hello, DevOps for all!"}

app.include_router(metrics.router)
app.include_router(aws.router, prefix="/aws")
 #Nedjsjsn 
