# AHK屏幕取色

按住F1取色，右上角显示颜色预览，松开复制颜色值。

```autohotkey
#NoEnv
#SingleInstance, force

CoordMode, Mouse
CoordMode, ToolTip, Screen
CoordMode, Pixel, Screen

SPI_GETMOUSESPEED = 0x70
SPI_SETMOUSESPEED = 0x71
GUISIZE = 65
MOUSESPEED = 5 ; range: 1-20 default: 10

$F1::
    DllCall("SystemParametersInfo", UInt, SPI_GETMOUSESPEED, UInt, 0, UIntP, OrigMouseSpeed, UInt, 0)
    DllCall("SystemParametersInfo", UInt, SPI_SETMOUSESPEED, UInt, 0, Ptr, MOUSESPEED, UInt, 0)
    Gosub, label_GetColor
Return

label_GetColor:
    Loop
    {
        Gui_x := A_ScreenWidth - GUISIZE * 2, Gui_y := GUISIZE
        Gui, +AlwaysOnTop +ToolWindow -Caption -DPIScale
        Gui, Show, NoActivate W%GUISIZE% H%GUISIZE% X%Gui_x% Y%Gui_y%
        WinSet, Transparent, Off
        if not GetKeyState("F1", "P")
        {
            DllCall("SystemParametersInfo", UInt, SPI_SETMOUSESPEED, UInt, 0, Ptr, OrigMouseSpeed, UInt, 0)
            Clipboard := StrReplace(Color_2, "0x", "#")
            SetTimer, RemoveToolTip, 1000
            break
        }
        Else
        {
            MouseGetPos , x, y
            PixelGetColor, Color_1, % x, % y, RGB ; 0xRRGGBB
            If Color_1 != %Color_2%
            {
                Color_2 := Color_1
                Gui, Color, % Color_2
            }
            ToolTip % StrReplace(Color_2, "0x", "#"), % Gui_x, GUISIZE * 2
        }
    }
Return

RemoveToolTip:
    SetTimer, RemoveToolTip, Off
    ToolTip
    Gui, Destroy
Return
```
