# GIT CLI

## 1 设置用户名密码

```bash

git config --global user.name "your username"
git config --global user.password "your password"
```

## 2 拉远程仓库代码并合并

``` bash
git pull origin master
```

## 3 提交代码到本地仓库

``` bash
# 查看有哪些改动
git status

# 添加所有改动
git add .

# 提交到本地仓库
git commit -m "your comments."
```

## 4 提交代码到远程仓库

```bash
git push -u origin master
```

## 5 分支和tag

```bash
# 查看分支
git branch -a

# 创建分支
git branch dev

# 切换本地分支
git checkout dev

# 从远程分支创建本地分支
git checkout -b dev origin/dev

# 创建tag
git tag v3.0
# 提交tag到远程分支
git push origin v3.0

# 远程tag创建分支
git checkout -b v3.0hotfix v3.0

```

## 6 设置git地址

```bash
# 查看git仓库
git remote -v

# 删除git仓库
git remote rm origin

# 添加git
git remote add origin git@github.com:LumiaSnow/SimpleBlog.git
```

