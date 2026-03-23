# AI Coding Hub 🚀

**一个账号，用遍所有 AI 编程模型**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 接入智谱 GLM、MiniMax、火山方舟等所有主流 AI 编程助手，统一计费，自动选择最优模型。

---

## ✨ 特性

- 🔑 **一个账号** - 无需注册多个平台
- 💰 **自动比价** - 智能选择最便宜的模型
- 📊 **统一统计** - 清晰查看使用量和花费
- 🛠️ **工具兼容** - 支持 Claude Code、Cline、Cursor 等

---

## 🎯 支持的平台

| 平台 | 模型 | 价格 |
|------|------|------|
| 智谱 GLM | GLM-4 / GLM-3-turbo | ¥0.005/1K tokens |
| MiniMax | abab6.5 / abab6 | ¥0.003/1K tokens |
| 火山方舟 | Doubao-pro / Doubao-lite | ¥0.002/1K tokens |

---

## 🚀 快速开始

### 方式一：Docker Compose（推荐）

```bash
git clone https://github.com/muyh89757/ai-coding-hub.git
cd ai-coding-hub
docker-compose up -d
```

访问：
- 后端 API: http://localhost:8000/docs
- 前端页面：http://localhost:3000

### 方式二：手动部署

**后端**
```bash
cd backend
pip install -r requirements.txt
python main.py
```

**前端**
```bash
cd frontend
npm install
npm run dev
```

---

## 📁 项目结构

```
ai-coding-hub/
├── backend/              # FastAPI 后端
│   ├── main.py          # 主程序
│   ├── database.py      # 数据库模型
│   ├── auth.py          # 用户认证
│   ├── providers/       # AI 平台接入
│   └── routes/          # API 路由
├── frontend/             # Next.js 前端
│   ├── app/             # App Router
│   ├── package.json     # 依赖配置
│   └── ...
├── Dockerfile           # Docker 镜像
├── docker-compose.yml   # Docker 编排
└── README.md            # 项目说明
```

---

## 💰 变现模式

| 套餐 | 价格 | 功能 |
|------|------|------|
| 免费版 | ¥0 | 基础模型访问 |
| 个人版 | ¥29/月 | 全模型访问 |
| 专业版 | ¥99/月 | 高限额 + 优先支持 |
| 团队版 | ¥299/月 | 多成员 + 管理后台 |

---

## 📊 开发进度

- [x] GitHub 仓库创建
- [x] 产品需求文档
- [x] FastAPI 后端框架
- [x] 数据库设计
- [x] 用户认证系统
- [x] 智谱 GLM API 接入
- [x] MiniMax API 接入
- [x] 火山方舟 API 接入
- [x] 统一 API 接口
- [x] 使用量统计 API
- [x] Docker 部署配置
- [x] 部署文档
- [ ] 前端页面开发
- [ ] 支付集成
- [ ] 生产环境部署

---

## 🛠️ 技术栈

**后端**: FastAPI, SQLAlchemy, JWT
**前端**: Next.js 14, TypeScript, Tailwind CSS
**数据库**: PostgreSQL / SQLite
**部署**: Docker, Docker Compose

---

## 📞 联系方式

- **GitHub**: https://github.com/muyh89757/ai-coding-hub
- **问题反馈**: 提交 Issue

---

## 📄 许可证

MIT License © 2026 muyh89757

**项目状态**: 🟢 开发中
**最后更新**: 2026-03-23
