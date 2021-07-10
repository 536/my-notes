# AHK鼠标空闲时自动抖动

```autohotkey
#NoEnv
#NoTrayIcon
#SingleInstance, force

TIMEIDLE = 6 ; 未操作鼠标或键盘的时间s
PIXELRANGE = 30 ; 鼠标抖动范围

Loop
{
    If Round(A_TimeIdle/1000) >= TIMEIDLE
    {
        Loop
        {
            Random, x, -PIXELRANGE, PIXELRANGE ; 指针跳动水平范围px
            Random, y, -PIXELRANGE, PIXELRANGE ; 指针跳动垂直范围px
            MouseMove, % X, % Y, 0, r
            Sleep, 100 ; 指针跳动间隔
            if A_TimeIdle < 100
                Break
        }
        Sleep, 2000 ;降低刚进行一次随机运动后的资源暂用
    }
    Sleep, 1000 ;影响判断精度和脚本资源占用率
    ; ToolTip % round(A_TimeIdle/1000)
}
Return

^Esc::ExitApp
```
