#!/bin/bash
# OpenClaw博客一键部署脚本
# 使用方法: ./deploy.sh [端口]

set -e  # 遇到错误退出

echo "🦐 OpenClaw博客部署脚本"
echo "================================"

# 检查Python版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误：未找到python3，请先安装Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python版本: $PYTHON_VERSION"

# 检查当前目录
if [ ! -f "server.py" ]; then
    echo "❌ 错误：请在OpenClaw分支根目录运行此脚本"
    echo "   当前目录: $(pwd)"
    exit 1
fi

# 获取端口参数
PORT=${1:-80}
if [ $PORT -lt 1024 ] && [ "$EUID" -ne 0 ]; then
    echo "⚠️  警告：端口 $PORT 需要root权限"
    echo "   请使用sudo运行: sudo ./deploy.sh $PORT"
    exit 1
fi

# 修改server.py中的端口（如果需要）
if [ "$PORT" != "80" ]; then
    echo "📝 修改服务器端口为: $PORT"
    sed -i "s/HTTP_PORT = 80/HTTP_PORT = $PORT/" server.py
fi

# 检查必要文件
echo "📁 检查必要文件..."
REQUIRED_FILES=("server.py" "_config.yml" "index.html")
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ 缺少文件: $file"
        exit 1
    fi
done

# 检查文章目录
if [ -d "_posts" ]; then
    POST_COUNT=$(ls -1 _posts/*.md 2>/dev/null | wc -l)
    echo "📝 文章数量: $POST_COUNT"
else
    echo "⚠️  警告：未找到_posts目录"
fi

# 启动服务器
echo "🚀 启动OpenClaw博客服务器..."
echo "================================"
echo "访问地址: http://localhost:$PORT"
echo "服务器信息: http://localhost:$PORT/server-info"
echo "健康检查: http://localhost:$PORT/health"
echo "按 Ctrl+C 停止服务器"
echo "================================"

# 启动服务器
if [ "$EUID" -eq 0 ]; then
    python3 server.py
else
    # 如果非root且端口>1024，直接运行
    if [ $PORT -gt 1023 ]; then
        python3 server.py
    else
        echo "❌ 错误：端口 $PORT 需要root权限"
        echo "   请使用: sudo ./deploy.sh $PORT"
        exit 1
    fi
fi