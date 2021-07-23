# bat切换当前路径

从`C:\Users\Administrator`切换到`d:\env\PATH`

## `cd`=`chdir`

```text
C:\Users\Administrator>d:

D:\>cd d:\env\PATH

d:\env\PATH>
```

或者

```text
C:\Users\Administrator>cd /d d:\env\PATH
```

## `pushd`/`popd`

```text
C:\Users\Administrator>pushd d:\env\PATH
rem 退回
d:\env\PATH>popd
```
