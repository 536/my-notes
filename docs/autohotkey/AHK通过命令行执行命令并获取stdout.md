# AHK通过命令行执行命令并获取stdout

```autohotkey
MsgBox, % WLAN() ;list all AP's in range with detailed info
MsgBox, % WLAN("ssids") ;list ONLY SSID's of all AP's in range
MsgBox, % WLAN("connect", "CODEMONKEY") ;connect to known(previously connected SSID)
MsgBox, % WLAN("setmode", "CODEMONKEY", "manual") ;set connection mode 'auto' or 'manual',i.e should windows automatically connect if it's in range
MsgBox, % WLAN("history") ;list previously connected AP's
MsgBox, % WLAN("disconnect") ;disconnect WiFi from any connection

;example to show how to connect to a wifi AP that has the string "home". For those new to autohotkey...
ssids := WLAN("ssids")
Loop, Parse, ssids, `n
    IfInString, A_LoopField, home
    MsgBox, % WLAN("connect", A_LoopField)

/*
Known Issue: given this is simply an ahk wrapper for netsh, To Connect to a An Access Point,
you need to connect to an AP 'MANUALLY AT LEAST ONCE' to connect to it using this function.

-->run with out params to display all AP's in range.
-->run disconnect param with out ssid,it disconnects any connection.
-->Connection mode can either be, 'manual' or 'auto'
-->Can Display All Connections in range, Connect/Disconnect, List of Previous Connections & Change connection modes.
*/

WLAN(command:=0, ssid:=0, mode="manual"){
    ;using IfEqual instead of 'If' only as it's more reliable without braces.
    If !command
        command = netsh wlan show networks mode=bssid
    IfEqual, command, ssids
    command = netsh wlan show networks mode=ssid
    IfEqual, command, connect
    command = netsh wlan connect name="%ssid%"
    IfEqual, command, disconnect
    command = netsh wlan disconnect
    IfEqual, command, history
    command = netsh wlan show profiles
    IfEqual, command, setmode
    command = netsh wlan set profileparameter name="%ssid%" connectionmode=%mode%

    vStdOut := RunCommand(command)

    IfEqual, command, netsh wlan show networks mode=ssid
    {
        Loop, Parse, vStdOut, `n
        {
            IfInString, A_LoopField, SSID
            {
                StringTrimLeft, this_loopField, A_LoopField, 9
                ssids .= this_loopField "`n"
            }
        }
        Return % ssids
    }
    Return % vStdOut
}

RunCommand(command) {
    DetectHiddenWindows, On
    Run, % ComSpec,, Hide, vPID
    WinWait, % "ahk_pid " vPID
    DllCall("kernel32\AttachConsole", UInt,vPID)
    oShell := ComObjCreate("WScript.Shell")
    oExec := oShell.Exec(ComSpec " /c " command )
    vStdOut := ""
    while !oExec.StdOut.AtEndOfStream
        vStdOut := oExec.StdOut.ReadAll()
    DllCall("kernel32\FreeConsole")
    Process, Close, % vPID
    Return vStdOut
}
```
