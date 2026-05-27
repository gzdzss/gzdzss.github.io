# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个基于 Hux Blog 主题的 Jekyll 个人博客，部署在 GitHub Pages (https://gzdzss.cn)。支持侧边栏布局、标签云、PWA 离线访问等功能。

## 常用命令

### 本地开发
```bash
# 启动 Jekyll 服务（带实时刷新和 LiveReload）
npm run start
# 或直接使用：
bundle exec jekyll serve -w -l --host 0.0.0.0

# 完整开发模式（包含 LESS/JS 文件监视）
npm run dev
```

### 构建
```bash
# 编译 LESS 和压缩 JS
grunt

# 构建 Jekyll 站点
bundle exec jekyll build

# 仅监视 LESS/JS 变化
grunt watch
```

### 部署
```bash
# 推送到 GitHub Pages（项目会自动部署）
git push origin gh-pages
```

## 项目架构

### 目录结构
- `_layouts/` - Jekyll 模板：`default.html`（基础）、`page.html`（带 banner 的页面）、`post.html`（博客文章）、`keynote.html`（全宽演讲稿）
- `_includes/` - 可复用 HTML 组件：导航栏、页脚、侧边栏、搜索框等
- `_posts/` - 博客文章（Markdown 格式）
- `less/` - LESS 样式源文件（编译到 `css/hux-blog.css`）
- `js/` - JavaScript 文件（`hux-blog.js` 是主要逻辑）
- `pwa/` - PWA 相关资源（manifest.json、图标）
- `_site/` - Jekyll 生成的静态站点输出（部署目标）

### 文章格式
文章存放在 `_posts/`，使用以下 front matter：
```yaml
---
layout: post
title: "文章标题"
date: YYYY-MM-DD HH:MM:SS +0800
categories: [分类1, 分类2]
tags: [标签1, 标签2]
---
```

文件命名规范：`YYYY-MM-DD-title-slug.md`

### 关键配置（`_config.yml`）
- Markdown 解析器：kramdown + GFM（GitHub Flavored Markdown）
- 代码高亮：rouge（代码块显示行号）
- 分页：每页 10 篇文章（jekyll-paginate）
- 侧边栏：已启用，显示头像和标签云
- PWA：Service Worker 已启用，支持离线访问

### 模板继承关系
`default.html` 是基础模板，所有页面都继承它。`page.html` 添加了带背景图的 intro-header。`post.html` 扩展 `page.html` 用于博客文章。

### CSS/样式开发
- LESS 文件位于 `less/`，编译后输出到 `css/hux-blog.css`
- 变量定义在 `less/variables.less`
- 修改 LESS 文件后需运行 `grunt less`

### 多语言支持
关于页面内容分为 `_includes/about/en.md` 和 `_includes/about/zh.md`。文章可通过 `lang: en` 设置语言，默认为中文（截断长度不同）。

## 注意事项

- `.gitignore` 排除了 `*.py` 文件（Python 测试文件）
- Gemfile 使用 Ruby China 镜像源
- 项目使用 gh-pages 分支部署