# git设置文件名大小写敏感

```bash
# 查看当前设置
git config --get core.ignorecase

# 修改设置
git config core.ignorecase false
```

## 删除远程仓库的指定文件夹

```bash
git rm -r --cached ./tags/PyQT  # --cached不会把本地的文件夹删除
git commit -m "remove dir ./tags/PyQT"
git push
```
