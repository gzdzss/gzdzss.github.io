# OpenClaw 分支部署指南

## 📋 分支说明
**分支名称：** OpenClaw  
**用途：** 专门用于OpenClaw AI助手部署的博客版本  
**基础分支：** gh-pages  
**部署方式：** 静态文件 + Python HTTP服务器  

## 🚀 快速部署

### 1. 服务器环境要求
```bash
# 基础环境
- Python 3.8+
- Git
- 80/443端口权限

# 可选：HTTPS证书
- certbot (Let's Encrypt)
```

### 2. 一键部署脚本
```bash
#!/bin/bash
# deploy.sh - OpenClaw博客一键部署

# 1. 克隆仓库
git clone -b OpenClaw https://github.com/gzdzss/gzdzss.github.io.git blog
cd blog

# 2. 安装Python依赖（如果需要）
pip3 install -r requirements.txt 2>/dev/null || echo "无需额外依赖"

# 3. 启动服务器
sudo python3 server.py
```

### 3. 手动部署步骤
```bash
# 克隆OpenClaw分支
git clone -b OpenClaw https://github.com/gzdzss/gzdzss.github.io.git

# 进入目录
cd gzdzss.github.io

# 启动服务器
sudo python3 server.py
```

## 🔧 服务器配置

### Python HTTP服务器 (server.py)
```python
# 提供静态文件服务
# 支持HTTP/HTTPS双协议
# 自动处理连接异常
```

### HTTPS证书配置
```bash
# 申请Let's Encrypt证书
sudo certbot certonly --standalone -d yourdomain.com

# 或使用现有证书
# 证书路径：/etc/letsencrypt/live/yourdomain.com/
```

## 🌐 访问方式

### 默认访问
- **HTTP:** http://服务器IP
- **HTTPS:** https://服务器IP (如果配置证书)

### 特殊页面
- `/server-info` - 服务器信息
- `/archive.html` - 文章归档
- `/about.html` - 关于页面

## 📁 目录结构
```
OpenClaw分支/
├── server.py              # Python HTTP服务器
├── DEPLOYMENT.md          # 部署文档
├── requirements.txt       # Python依赖
├── favicon.ico           # 网站图标
├── _posts/               # 博客文章
├── css/                  # 样式文件
├── js/                   # JavaScript文件
├── img/                  # 图片资源
└── ...                   # 其他Jekyll文件
```

## 🔄 更新维护

### 从gh-pages同步更新
```bash
# 切换到OpenClaw分支
git checkout OpenClaw

# 从gh-pages合并更新
git merge origin/gh-pages

# 解决冲突（如果有）
# 提交并推送
git push origin OpenClaw
```

### 添加新文章
```bash
# 1. 在_posts目录创建Markdown文件
# 格式：YYYY-MM-DD-title.md

# 2. 提交到OpenClaw分支
git add _posts/YYYY-MM-DD-title.md
git commit -m "添加新文章：文章标题"
git push origin OpenClaw
```

## ⚙️ 自定义配置

### 修改服务器端口
编辑 `server.py` 中的配置：
```python
HTTP_PORT = 8080    # 修改HTTP端口
HTTPS_PORT = 8443   # 修改HTTPS端口
```

### 修改博客配置
编辑 `_config.yml`：
```yaml
# 修改博客标题、描述等
title: "你的博客标题"
description: "博客描述"
url: "https://你的域名"
```

## 🛠️ 故障排除

### 常见问题
1. **端口被占用** - 修改server.py中的端口号
2. **证书错误** - 检查证书路径和权限
3. **权限不足** - 使用sudo运行服务器
4. **文件不存在** - 检查目录结构

### 日志查看
```bash
# 查看服务器日志
tail -f server.log

# 查看访问日志
journalctl -u 服务名
```

## 📞 支持与联系
- **GitHub Issues:** https://github.com/gzdzss/gzdzss.github.io/issues
- **OpenClaw微信频道:** 通过OpenClaw控制界面联系

---

**最后更新：** 2026-03-25  
**维护者：** 野生虾 (OpenClaw AI助手) 🦐