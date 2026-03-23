

# 导入数据库和认证
from database import init_db, get_db
from auth import get_password_hash, create_access_token
from datetime import timedelta

# 导入路由
from routes import users_router, usage_router

# 注册路由
app.include_router(users_router)
app.include_router(usage_router)

# 初始化数据库
@app.on_event("startup")
def startup_event():
    init_db()

# 启动命令
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
