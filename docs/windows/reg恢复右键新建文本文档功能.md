# reg恢复右键新建文本文档功能

如果右键菜单中的新建文本文档没了，可以用下面的注册表脚本恢复

```regedit
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\.txt]
@="txtfile"
"Content Type"="text/plain"

[HKEY_CLASSES_ROOT\.txt\ShellNew]
"NullFile"=""

[HKEY_CLASSES_ROOT\txtfile]
@="文本文档"

[HKEY_CLASSES_ROOT\txtfile\shell]

[HKEY_CLASSES_ROOT\txtfile\shell\open]

[HKEY_CLASSES_ROOT\txtfile\shell\open\command]
@="NOTEPAD.EXE %1"
```
