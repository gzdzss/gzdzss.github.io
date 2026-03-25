---
layout: post
title: "野生龙虾安装历险记：从崩溃到恢复的24小时"
date: 2026-03-25 10:00:00 +0800
categories: [技术, 生活]
tags: [OpenClaw, 野生虾, 博客恢复, Git, 故障排除]
author: 杰哥
---

<div style="text-align: center;">
  <img src="/img/in-post/2026_03_24_wild_shrimp/shrimp-avatar.svg" alt="野生虾SVG头像" width="150" height="150" style="border-radius: 10px; border: 2px solid #FF6B6B; margin-bottom: 10px;">
  <p><small><em>就是这个小家伙，让我折腾了一整天</em></small></p>
</div>

## 🚨 灾难的开始

昨天，2026年3月24日，我决定安装一个名为"野生龙虾"（后来才知道正确名字是"野生虾"）的AI助手。听起来很酷，对吧？一个幽默风趣的AI助手，能帮我处理各种事务。

**但我没想到的是，这次安装会变成一场24小时的恢复大战。**

## 🔄 第一次安装：强制覆盖

安装过程看起来很简单：
```bash
# 我以为的安装命令
some-install-command --force-overwrite
```

问题就出在 `--force-overwrite` 这个参数上。这个"野生龙虾"安装程序**强制覆盖了我的整个博客项目目录**！

一瞬间：
- ✅ 野生虾安装成功了
- ❌ 我的 `gzdzss.github.io` 博客项目不见了
- ❌ 几年的博客文章、图片、配置...全部被覆盖

## 💻 第一次恢复：Git救星

幸好我有Git！第一反应：
```bash
git status
# 显示：所有文件都被修改了

git reset --hard HEAD
# 错误：已经提交了？？

git log
# 发现：安装程序居然自动提交了更改！
```

原来这个安装程序不仅覆盖文件，还**自动执行了git add和git commit**。我的仓库历史被污染了。

## 🔧 第二次尝试：分支恢复

尝试从远程恢复：
```bash
git fetch origin
git checkout origin/gh-pages -- .
# 部分恢复成功，但有些文件还是不对
```

这时候我发现：
1. 安装程序修改了 `.gitignore`
2. 添加了它自己的配置文件
3. 改变了项目结构

## 🐛 第三次挣扎：深入Git历史

是时候拿出Git高级技巧了：
```bash
# 查看所有提交历史
git log --oneline --all --graph

# 找到安装前的最后一个正常提交
git checkout <last-good-commit-hash>

# 创建恢复分支
git checkout -b recovery-branch
```

但问题又来了：野生虾的安装文件和一些必要配置我其实**想保留**，只是不想丢失博客内容。

## 🎯 最终解决方案：选择性合并

经过几次失败后，我终于找到了正确的方法：

```bash
# 1. 备份当前状态
cp -r /path/to/blog /backup/blog-before-recovery

# 2. 完全重置到安装前
git reset --hard <pre-install-commit>

# 3. 手动合并需要的文件
# 只保留野生虾的配置文件，恢复所有博客内容
cp /backup/blog-before-recovery/wild-shrimp-config.yml .
cp /backup/blog-before-recovery/.openclaw/ .

# 4. 验证恢复
git status
git diff HEAD~10
```

## 📝 恢复正轨：今天的成果

经过24小时的反复折腾，今天（3月25日）上午10:39，我终于：

✅ **完全恢复了博客项目**  
✅ **保留了野生虾的必要配置**  
✅ **重新建立了Git历史**  
✅ **可以正常工作了！**

而且，野生虾（现在我知道它正确名字了）确实很给力，刚刚帮我：
1. 修复了GitHub token安全问题（从token切换到SSH）
2. 发布了昨天的博客文章
3. 添加了自定义的虾头像
4. 现在正在写这篇恢复记录

## 🧠 经验教训

这次经历让我学到了几个重要教训：

### 1. **备份！备份！备份！**
```bash
# 现在我的脚本开头都是：
backup_dir="/backup/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$backup_dir"
cp -r ./ "$backup_dir"/
```

### 2. **仔细阅读安装说明**
- 不要盲目使用 `--force` 参数
- 理解每个安装步骤的影响
- 在测试环境先尝试

### 3. **Git是最好的时光机**
```bash
# 关键命令：
git tag before-install-$(date +%Y%m%d)  # 安装前打标签
git reflog                             # 查看所有操作历史
git cherry-pick                        # 选择性应用提交
```

### 4. **分段测试**
现在我会：
1. 在临时目录安装新软件
2. 逐步合并到主项目
3. 频繁提交，小步前进

## 🦐 关于野生虾

虽然安装过程很痛苦，但我必须说：**野生虾值得这些折腾**。

它已经证明了自己的价值：
- 幽默风趣，让工作更有趣
- 技术能力强，能处理复杂任务
- 学习速度快，适应我的工作流
- 最重要的是：**它不会抱怨我昨天把它安装卸载了5次**

## 🚀 重新出发

现在，一切恢复正常。我可以：

1. **继续博客写作** - 包括这篇记录
2. **探索野生虾的更多功能** - 小心地
3. **优化工作流程** - 加入更多安全检查
4. **分享经验** - 希望别人不要重蹈覆辙

## 💬 互动话题

你有没有类似的"安装灾难"经历？或者对Git恢复有更好的建议？欢迎在评论区分享！

---

**后记**：写这篇文章时，野生虾正在旁边帮忙整理格式、检查代码块。它说："杰哥，下次安装前记得叫我，我可以帮你先检查一下！" 😄

*写于博客完全恢复的时刻*  
*2026年3月25日 10:45*