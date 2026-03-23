# AI Coding Hub - 部署指南

## 方式一：Docker Compose（推荐）

```bash
git clone https://github.com/muyh89757/ai-coding-hub.git
cd ai-coding-hub
docker-compose up -d
```

访问：
- 后端 API: http://localhost:8000/docs
- 前端页面：http://localhost:3000

## 方式二：手动部署

### 后端
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### 前端
```bash
cd frontend
npm install
npm run dev
```

## 环境变量

编辑 `backend/.env`：
```env
DATABASE_URL=sqlite:///./ai_coding_hub.db
JWT_SECRET_KEY=your-secret-key
ZHIPU_API_KEY=your_zhipu_api_key
```

## 系统要求

- 最低：2 核 CPU, 4GB 内存
- 推荐：4 核 CPU, 8GB 内存
