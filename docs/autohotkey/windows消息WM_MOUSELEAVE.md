# windows消息WM_MOUSELEAVE

<https://www.autohotkey.com/boards/viewtopic.php?f=76&t=48194&p=215653&hilit=WM_MOUSELEAVE#p215653>

```autohotkey
OnMessage(0x200, "OnMouseMove")

gui, +hwndguiId

; This doesn't work on 64 bit
/*
typedef struct tagTRACKMOUSEEVENT {
    DWORD cbSize;
    DWORD dwFlags;
    HWND hwndTrack;
    DWORD dwHoverTime;
} TRACKMOUSEEVENT, *LPTRACKMOUSEEVENT;
*/

WM_MOUSELEAVE:=0x2A3
cbSize:=A_PtrSize=4?16:24
TME_LEAVE:=0x00000002
dwFlags:=TME_LEAVE

VarSetCapacity(TRACKMOUSEEVENT, cbSize,0)
NumPut(cbSize, TRACKMOUSEEVENT, 0, "Uint")
NumPut(dwFlags, TRACKMOUSEEVENT, 4, "Uint")
NumPut(guiId, TRACKMOUSEEVENT, 8, "Ptr")
; NumPut(0, TRACKMOUSEEVENT, 8+A_PtrSize, "Uint") ; Not needed

if !DllCall("User32.dll\TrackMouseEvent", "Ptr", &TRACKMOUSEEVENT)
    Msgbox fail
else
    OnMessage(WM_MOUSELEAVE, "WM_MOUSELEAVE")

gui, show, w200 h200

OnMouseMove(){
    global TRACKMOUSEEVENT
    OnMessage(0x200, "OnMouseMove", 0)
    DllCall("User32.dll\TrackMouseEvent", "Ptr", &TRACKMOUSEEVENT)
    ToolTip % "Mouse entered gui @ " A_TickCount,0,0
}

WM_MOUSELEAVE(){
    ToolTip, % "Mouse left gui @ " A_TickCount,0,0
    OnMessage(0x200, "OnMouseMove")
}
```
