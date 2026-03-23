# AI Coding Hub - 后端服务

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

# 初始化应用
app = FastAPI(
    title="AI Coding Hub API",
    description="AI 编程助手聚合平台后端 API",
    version="0.1.0"
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class User(BaseModel):
    id: int
    username: str
    email: str
    plan: str = "free"

class UsageRecord(BaseModel):
    user_id: int
    provider: str
    tokens_used: int
    cost: float

# 模拟数据库
fake_users_db = {
    1: {"id": 1, "username": "admin", "email": "admin@example.com", "plan": "pro"}
}

fake_usage_db = []

# API 路由
@app.get("/")
async def root():
    return {"message": "Welcome to AI Coding Hub API", "version": "0.1.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in fake_users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return fake_users_db[user_id]

@app.post("/usage/")
async def record_usage(user_id: int, provider: str, tokens_used: int, cost: float):
    from datetime import datetime
    record = {
        "user_id": user_id,
        "provider": provider,
        "tokens_used": tokens_used,
        "cost": cost,
        "timestamp": datetime.now().isoformat()
    }
    fake_usage_db.append(record)
    return {"message": "Usage recorded", "record": record}

@app.get("/providers")
async def list_providers():
    return {
        "providers": [
            {"name": "智谱 GLM", "endpoint": "https://open.bigmodel.cn/api/paas/v4/"},
            {"name": "MiniMax", "endpoint": "https://api.minimax.chat/v1/"},
            {"name": "火山方舟", "endpoint": "https://ark.cn-beijing.volces.com/api/v3/"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
