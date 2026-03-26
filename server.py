#!/usr/bin/env python3
"""
OpenClaw分支专用服务器
基于Jekyll静态博客的HTTP/HTTPS服务器
"""

import http.server
import ssl
import socketserver
import os
import sys
from datetime import datetime

# ==================== 配置区域 ====================
# 修改以下配置以适应你的环境

# 服务器配置
HTTP_PORT = 80          # HTTP端口（需要root权限）
HTTPS_PORT = 443        # HTTPS端口（需要root权限）
SERVER_IP = "0.0.0.0"   # 监听所有IP地址

# 博客目录（自动设置为当前目录）
BLOG_DIR = os.path.dirname(os.path.abspath(__file__))

# HTTPS证书配置（可选）
# 如果需要HTTPS，取消注释并修改以下配置
# CERT_DIR = "/etc/letsencrypt/live/yourdomain.com"
# CERT_FILE = os.path.join(CERT_DIR, "fullchain.pem")
# KEY_FILE = os.path.join(CERT_DIR, "privkey.pem")

# ==================== 服务器代码 ====================

class OpenClawHandler(http.server.SimpleHTTPRequestHandler):
    """OpenClaw博客处理器"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BLOG_DIR, **kwargs)
    
    def do_GET(self):
        """处理GET请求"""
        # 特殊路由处理
        if self.path == '/server-info':
            return self.send_server_info()
        if self.path == '/health':
            return self.send_health_check()
        
        # 默认处理静态文件
        try:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)
        except (ConnectionResetError, BrokenPipeError):
            # 忽略连接重置错误（客户端中断连接）
            pass
        except Exception as e:
            self.send_error(500, f"Server error: {str(e)}")
    
    def send_server_info(self):
        """显示服务器信息页面"""
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        
        # 获取博客信息
        posts_dir = os.path.join(BLOG_DIR, "_posts")
        if os.path.exists(posts_dir):
            post_count = len([f for f in os.listdir(posts_dir) if f.endswith('.md')])
            latest_posts = sorted([f for f in os.listdir(posts_dir) if f.endswith('.md')], reverse=True)[:3]
        else:
            post_count = 0
            latest_posts = []
        
        server_info = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>OpenClaw博客服务器信息</title>
            <style>
                body {{ font-family: 'Segoe UI', Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }}
                .container {{ max-width: 1000px; margin: 0 auto; background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 20px; backdrop-filter: blur(10px); }}
                h1 {{ text-align: center; margin-bottom: 30px; }}
                .card {{ background: rgba(255, 255, 255, 0.15); padding: 20px; border-radius: 10px; margin: 20px 0; }}
                .stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }}
                .stat {{ background: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px; text-align: center; }}
                .stat h3 {{ margin: 0 0 10px 0; color: #4CAF50; }}
                .stat-value {{ font-size: 2em; font-weight: bold; }}
                .shrimp {{ font-size: 4em; text-align: center; animation: bounce 2s infinite; }}
                @keyframes bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-20px); }} }}
                .btn {{ display: inline-block; background: #4CAF50; color: white; padding: 10px 20px; margin: 5px; border-radius: 5px; text-decoration: none; transition: background 0.3s; }}
                .btn:hover {{ background: #45a049; }}
                code {{ background: rgba(0, 0, 0, 0.3); padding: 2px 6px; border-radius: 3px; font-family: 'Courier New', monospace; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="shrimp">🦐</div>
                <h1>OpenClaw博客服务器</h1>
                
                <div class="card">
                    <h2>📊 服务器状态</h2>
                    <div class="stats">
                        <div class="stat">
                            <h3>文章数量</h3>
                            <div class="stat-value">{post_count}</div>
                        </div>
                        <div class="stat">
                            <h3>HTTP端口</h3>
                            <div class="stat-value">{HTTP_PORT}</div>
                        </div>
                        <div class="stat">
                            <h3>HTTPS端口</h3>
                            <div class="stat-value">{HTTPS_PORT}</div>
                        </div>
                        <div class="stat">
                            <h3>运行时间</h3>
                            <div class="stat-value" id="uptime">--</div>
                        </div>
                    </div>
                </div>
                
                <div class="card">
                    <h2>📝 最新文章</h2>
                    <ul>
                        {"".join([f'<li>{post.replace(".md", "")}</li>' for post in latest_posts[:5]])}
                    </ul>
                </div>
                
                <div class="card">
                    <h2>🔗 快速链接</h2>
                    <p>
                        <a href="/" class="btn">博客首页</a>
                        <a href="/archive.html" class="btn">文章归档</a>
                        <a href="/about.html" class="btn">关于作者</a>
                        <a href="/health" class="btn">健康检查</a>
                    </p>
                </div>
                
                <div class="card">
                    <h2>⚙️ 技术信息</h2>
                    <p><strong>分支：</strong> OpenClaw (专门用于OpenClaw部署)</p>
                    <p><strong>博客引擎：</strong> Jekyll静态生成器</p>
                    <p><strong>服务器：</strong> Python HTTP/HTTPS服务器</p>
                    <p><strong>源码仓库：</strong> <a href="https://github.com/gzdzss/gzdzss.github.io/tree/OpenClaw" style="color: #4CAF50;">gzdzss/gzdzss.github.io</a></p>
                    <p><strong>部署时间：</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
                
                <div class="card">
                    <h2>🚀 部署命令</h2>
                    <pre style="background: rgba(0,0,0,0.3); padding: 15px; border-radius: 5px; overflow-x: auto;">
# 克隆OpenClaw分支
git clone -b OpenClaw https://github.com/gzdzss/gzdzss.github.io.git

# 启动服务器
cd gzdzss.github.io
sudo python3 server.py</pre>
                </div>
                
                <div style="margin-top: 30px; text-align: center; color: rgba(255,255,255,0.7);">
                    <p>🦐 由野生虾(OpenClaw AI助手)维护 | 最后更新: 2026-03-25</p>
                </div>
            </div>
            
            <script>
                // 更新运行时间
                const startTime = new Date();
                function updateUptime() {{
                    const now = new Date();
                    const diff = now - startTime;
                    const hours = Math.floor(diff / 3600000);
                    const minutes = Math.floor((diff % 3600000) / 60000);
                    const seconds = Math.floor((diff % 60000) / 1000);
                    document.getElementById('uptime').textContent = 
                        `${{hours.toString().padStart(2, '0')}}:${{minutes.toString().padStart(2, '0')}}:${{seconds.toString().padStart(2, '0')}}`;
                }}
                updateUptime();
                setInterval(updateUptime, 1000);
            </script>
        </body>
        </html>
        """
        
        self.wfile.write(server_info.encode('utf-8'))
    
    def send_health_check(self):
        """健康检查接口"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        health_status = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "service": "OpenClaw Blog Server",
            "version": "1.0.0",
            "blog_posts": post_count if 'post_count' in locals() else 0,
            "server_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        import json
        self.wfile.write(json.dumps(health_status, indent=2).encode('utf-8'))
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        protocol = "HTTPS" if hasattr(self.server, 'ssl_context') and self.server.ssl_context else "HTTP"
        client_ip = self.address_string().split(':')[0]
        print(f"[{timestamp}] {protocol} {client_ip} - {format % args}")

def start_http_server():
    """启动HTTP服务器"""
    try:
        with socketserver.TCPServer((SERVER_IP, HTTP_PORT), OpenClawHandler) as httpd:
            httpd.ssl_context = None
            print(f"✅ OpenClaw博客HTTP服务器已启动")
            print(f"   📍 监听地址: {SERVER_IP}:{HTTP_PORT}")
            print(f"   📚 博客目录: {BLOG_DIR}")
            print(f"   🔗 访问地址: http://localhost:{HTTP_PORT}")
            print(f"   📊 服务器信息: http://localhost:{HTTP_PORT}/server-info")
            httpd.serve_forever()
    except Exception as e:
        print(f"❌ HTTP服务器启动失败: {e}")
        return None

def start_https_server():
    """启动HTTPS服务器（可选）"""
    try:
        # 检查证书配置
        if 'CERT_FILE' not in globals() or not os.path.exists(CERT_FILE):
            print(f"⚠️  HTTPS证书未配置，跳过HTTPS服务")
            print(f"   如需HTTPS，请配置CERT_FILE和KEY_FILE")
            return None
        
        # 创建SSL上下文
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
        
        # 创建HTTPS服务器
        with socketserver.TCPServer((SERVER_IP, HTTPS_PORT), OpenClawHandler) as httpsd:
            httpsd.socket = context.wrap_socket(httpsd.socket, server_side=True)
            httpsd.ssl_context = context
            print(f"✅ OpenClaw博客HTTPS服务器已启动")
            print(f"   📍 监听地址: {SERVER_IP}:{HTTPS_PORT}")
            print(f"   🔐 访问地址: https://localhost:{HTTPS_PORT}")
            print(f"   📊 服务器信息: https://localhost:{HTTPS_PORT}/server-info")
            httpsd.serve_forever()
    except Exception as e:
        print(f"❌ HTTPS服务器启动失败: {e}")
        return None

def main():
    """主函数"""
    print("=" * 60)
    print("🦐 OpenClaw博客部署服务器")
    print("=" * 60)
    print(f"分支版本: OpenClaw (专门部署版)")
    print(f"博客目录: {BLOG_DIR}")
    print(f"HTTP端口: {HTTP_PORT}")
    print(f"HTTPS端口: {HTTPS_PORT} {'(已配置)' if 'CERT_FILE' in globals() else '(未配置)'}")
    print(f"监听地址: {SERVER_IP}")
    print(f"启动时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # 检查权限（80/443端口需要root）
    if (HTTP_PORT < 1024 or HTTPS_PORT < 1024) and os.geteuid() != 0:
        print("❌ 错误：需要root权限来绑定1024以下端口")
        print("   请使用sudo运行此脚本，或修改端口号大于1024")
        sys.exit(1)
    
    print("启动服务器中...")
    
    # 使用多线程同时运行HTTP和HTTPS服务器
    import threading
    
    http_thread = threading.Thread(target=start_http_server, daemon=True)
    https_thread = threading.Thread(target=start_https_server, daemon=True)
    
    http_thread.start()
    https_thread.start()
    
    print("=" * 60)
    print("🎉 OpenClaw博客部署完成！")
    print(f"🌐 访问方式:")
    print(f"   1. 博客首页: http://localhost:{HTTP_PORT}")
    if 'CERT_FILE' in globals() and os.path.exists(CERT_FILE):
        print(f"   2. HTTPS访问: https://localhost:{HTTPS_PORT}")
    print(f"   3. 服务器信息: http://localhost:{HTTP_PORT}/server-info")
    print(f"   4. 健康检查: http://localhost:{HTTP_PORT}/health")
    print("=" * 60)
    print("📝 使用说明:")
    print("   - 按 Ctrl+C 停止服务器")
    print("   - 修改server.py中的配置以适应你的环境")
    print("   - 查看DEPLOYMENT.md获取详细部署指南")
    print("=" * 60)
    
    try:
        # 保持主线程运行
        while True:
            if not http_thread.is_alive():
                print("⚠️  HTTP服务器已停止")
            if not https_thread.is_alive():
                print("⚠️  HTTPS服务器已停止")
            if not http_thread.is_alive() and not https_thread.is_alive():
                print("❌ 所有服务器已停止")
                break
            threading.Event().wait(5)
    except KeyboardInterrupt:
        print("\n🛑 正在停止服务器...")
        sys.exit(0)

if __name__ == "__main__":
    main()