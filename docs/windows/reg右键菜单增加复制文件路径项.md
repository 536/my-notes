# reg右键菜单增加`复制文件路径`项

首先明确一点，按住`shift`加右键菜单中的`复制为路径`是否符合需求，如果不符合需求再使用下面的注册表脚本

## 文件-增加

```regedit
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\*\shell\lujin]
@="复制文件路径"
"Icon"="Shell32.dll,70"

[HKEY_CLASSES_ROOT\*\shell\lujin\command]
@="mshta vbscript:clipboarddata.setdata(\"text\",\"%1\")(close)"
```

## 文件-移除

```regedit
Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\*\shell\lujin]
@="复制文件路径"
"Icon"="Shell32.dll,70"

[-HKEY_CLASSES_ROOT\*\shell\lujin\command]
@="mshta vbscript:clipboarddata.setdata(\"text\",\"%1\")(close)"
```

## 文件夹-增加

```regedit
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\lujin]
@="复制文件夹路径"
"Icon"="Shell32.dll,4"

[HKEY_CLASSES_ROOT\Directory\Background\shell\lujin\command]
@="mshta vbscript:clipboarddata.setdata(\"text\",\"%v\")(close)"
```

## 文件夹-移除

```regedit
Windows Registry Editor Version 5.00

[-HKEY_CLASSES_ROOT\Directory\Background\shell\lujin]
@="复制文件夹路径"
"Icon"="Shell32.dll,4"

[-HKEY_CLASSES_ROOT\Directory\Background\shell\lujin\command]
@="mshta vbscript:clipboarddata.setdata(\"text\",\"%v\")(close)"
```
