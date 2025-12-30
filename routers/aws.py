from fastapi import APIRouter
from services.aws_service import get_bucket_info

router = APIRouter()

@router.get("/s3",status_code=200)
def get_buckets():

    try:
        buckets_info = get_bucket_info()
        return buckets_info
    except:
        raise HTTPException(
            status_code=500, 
            detail="Error retrieving system metrics"
        )