# AHK隐藏任务栏

```autohotkey
; 隐藏和显示任务栏
IfWinNotExist, ahk_class Shell_TrayWnd
{
    WinShow, ahk_class Shell_TrayWnd
    NumPut( ABS_ALWAYSONTOP, Off+24)
    DllCall("Shell32.dll\SHAppBarMessage", UInt,ABM_SETSTATE, UInt, &APPBARDATA)
}
Else
{
    WinHide, ahk_class Shell_TrayWnd
    NumPut( ABS_AUTOHIDE|ABS_ALWAYSONTOP, Off+24)
    DllCall("Shell32.dll\SHAppBarMessage", UInt,ABM_SETSTATE, UInt, &APPBARDATA)
}
```
