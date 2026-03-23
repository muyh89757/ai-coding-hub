# 使用量统计 API
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db, UsageRecord

router = APIRouter(prefix="/api/usage", tags=["usage"])

@router.get("/")
def get_usage(limit: int = 100, db: Session = Depends(get_db)):
    records = db.query(UsageRecord).order_by(UsageRecord.created_at.desc()).limit(limit).all()
    return {"records": [{"provider": r.provider, "tokens": r.tokens_used, "cost": r.cost} for r in records]}

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(UsageRecord).count()
    return {"total_requests": total}
