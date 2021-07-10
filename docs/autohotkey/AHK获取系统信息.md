# AHK获取系统信息

## 获取硬盘序列号

```autohotkey
objWMIService := ComObjGet("winmgmts:\\.\root\cimv2")
colItems := objWMIService.ExecQuery("SELECT * FROM Win32_PhysicalMedia")._NewEnum
while colItems[objItem]
{
    MsgBox, % objItem.SerialNumber
}
```

## 获取硬盘相关信息

```autohotkey
FileSelectFolder, folder, , 3, Pick a drive to analyze:
if not folder
    return
DriveGet, list, List
DriveGet, cap, Capacity, %folder%
DriveSpaceFree, free, %folder%
DriveGet, fs, FileSystem, %folder%
DriveGet, label, Label, %folder%
DriveGet, serial, Serial, %folder%
DriveGet, type, Type, %folder%
DriveGet, status, Status, %folder%
MsgBox All Drives: %list%`nSelected Drive: %folder%`nDrive Type: %type%`nStatus: %status%`nCapacity: %cap% M`nFree Space: %free% M`nFilesystem: %fs%`nVolume Label: %label%`nSerial Number: %serial%
```

## 显示每个监视器的信息

```autohotkey
SysGet, MonitorCount, MonitorCount
SysGet, MonitorPrimary, MonitorPrimary
MsgBox, Monitor Count:`t%MonitorCount%`nPrimary Monitor:`t%MonitorPrimary%
Loop, %MonitorCount%
{
    SysGet, MonitorName, MonitorName, %A_Index%
    SysGet, Monitor, Monitor, %A_Index%
    SysGet, MonitorWorkArea, MonitorWorkArea, %A_Index%
    MsgBox, Monitor:`t#%A_Index%`nName:`t%MonitorName%`nLeft:`t%MonitorLeft% (%MonitorWorkAreaLeft% work)`nTop:`t%MonitorTop% (%MonitorWorkAreaTop% work)`nRight:`t%MonitorRight% (%MonitorWorkAreaRight% work)`nBottom:`t%MonitorBottom% (%MonitorWorkAreaBottom% work)
}
```

## 获取电量

```autohotkey
objWMIService := ComObjGet("winmgmts:\\.\root\cimv2")
colItems := objWMIService.ExecQuery("select * from Win32_Battery")._NewEnum
while colItems[objItem]
{
    MsgBox, % objItem.EstimatedChargeRemaining
}
```

## 获取系统信息

```autohotkey
;~ http://msdn.microsoft.com/en-us/library/windows/desktop/ms724958%28v=vs.85%29.aspx
VarSetCapacity(structSysInfo,36)
DllCall("GetNativeSystemInfo",Uint,&structSysInfo)
wProcessorArchitectur	:= Numget(structSysInfo,0,"Short")
wReserved	:= Numget(structSysInfo,2,"Short")
dwPageSize	:= Numget(structSysInfo,4)
/*
  LPVOID lpMinimumApplicationAddress;	8-11
  LPVOID lpMaximumApplicationAddress;	12-15
  DWORD_PTR dwActiveProcessorMask;	16-19
*/
dwNumberOfProcessors	:= Numget(structSysInfo,20)
dwProcessorType	:= Numget(structSysInfo,24)
dwAllocationGranularity	:= Numget(structSysInfo,28) ;虚拟内存空间的粒度(Windows都是65536)
wProcessorLevel	:= Numget(structSysInfo,32,"Short")
wProcessorRevision	:= Numget(structSysInfo,34,"Short")
;处理数据
ProcessorArchitectur := wProcessorArchitectur=0 ? "32-bit (x86) System " : wProcessorArchitectur=9 ? "64-bit (x64 AMD or Intel)" : wProcessorArchitectur=6 ? "Intel Itanium-based" : "Unknown System"
SetFormat,integer,H
Model := wProcessorRevision >> 8
SetFormat,integer,d
Stepping := wProcessorRevision&0xFF
;
MsgBox,% "CPU体系结构: " ProcessorArchitectur "`n页大小: " dwPageSize " byte`nCPU数目: " dwNumberOfProcessors "`nCPU等级: " wProcessorLevel "`nCPU型号: " Model "`n步进: " Stepping
```

## 获取MAC地址

```autohotkey
;获取网卡硬件地址
MsgBox % "MAC地址：`n" GetMacAddress()

;方法一
GetMacAddress()
{
    NetworkConfiguration:=ComObjGet("Winmgmts:").InstancesOf("Win32_NetworkAdapterConfiguration")
    for mo in NetworkConfiguration
    {
        if(mo.IPEnabled <> 0)
            return mo.MacAddress
    }
}
; ;方法二
; GetMacAddress()
; {
; RunWait, %ComSpec% /c getmac /NH | clip,,hide
; RegExMatch(clipboard, ".*?([0-9A-Z].{16})(?!\w\\Device)", mac)
; return %mac1%
; }
; ;方法三
; GetMacAddress()
; {
; NetworkConfiguration := StdoutToVar_CreateProcess("getmac")
; RegExMatch(NetworkConfiguration, ".*?([0-9A-Z].{16})(?!\w\\Device)", mac)
; return %mac1%
; }

; ; Im Original gilt "CP0"; zu CharSet CP850/CP858 vgl.: https://goo.gl/Y8xUYu , http://goo.gl/cMtc6i , https://goo.gl/ssCplI , https://goo.gl/s2P1jK
; StdoutToVar_CreateProcess(sCmd, sEncoding:="CP858", sDir:="", ByRef nExitCode:=0) {
; DllCall( "CreatePipe", PtrP,hStdOutRd, PtrP,hStdOutWr, Ptr,0, UInt,0 )
; DllCall( "SetHandleInformation", Ptr,hStdOutWr, UInt,1, UInt,1 )

; VarSetCapacity( pi, (A_PtrSize == 4) ? 16 : 24, 0 )
; siSz := VarSetCapacity( si, (A_PtrSize == 4) ? 68 : 104, 0 )
; NumPut( siSz, si, 0, "UInt" )
; NumPut( 0x100, si, (A_PtrSize == 4) ? 44 : 60, "UInt" )
; NumPut( hStdInRd, si, (A_PtrSize == 4) ? 56 : 80, "Ptr" )
; NumPut( hStdOutWr, si, (A_PtrSize == 4) ? 60 : 88, "Ptr" )
; NumPut( hStdOutWr, si, (A_PtrSize == 4) ? 64 : 96, "Ptr" )

; if ( !DllCall( "CreateProcess", Ptr,0, Ptr,&sCmd, Ptr,0, Ptr,0, Int,True, UInt,0x08000000
; , Ptr,0, Ptr,sDir?&sDir:0, Ptr,&si, Ptr,&pi ) )
; return ""
; , DllCall( "CloseHandle", Ptr,hStdOutWr )
; , DllCall( "CloseHandle", Ptr,hStdOutRd )

; DllCall( "CloseHandle", Ptr,hStdOutWr ) ; The write pipe must be closed before Reading the stdout.
; VarSetCapacity(sTemp, 4095)
; while ( DllCall( "ReadFile", Ptr,hStdOutRd, Ptr,&sTemp, UInt,4095, PtrP,nSize, Ptr,0 ) )
; sOutput .= StrGet(&sTemp, nSize, sEncoding)

; DllCall( "GetExitCodeProcess", Ptr,NumGet(pi,0), UIntP,nExitCode )
; DllCall( "CloseHandle", Ptr,NumGet(pi,0) )
; DllCall( "CloseHandle", Ptr,NumGet(pi,A_PtrSize) )
; DllCall( "CloseHandle", Ptr,hStdOutRd )
; return sOutput
; }
```

## 获取CPU序列号

```autohotkey
MsgBox % "CPU序列号：`n" GetCpuID()

; 方法一
GetCpuID()
{
    objSWbemObject:=ComObjGet("winmgmts:Win32_Processor.DeviceID='cpu0'")
    return % objSWbemObject.ProcessorId
}
; ; 方法二
; GetCpuID()
; {
; 序列号:=objSWbemObject.ProcessorId
; 命令:="wmic cpu get Processorid"
; RunWait, %ComSpec% /c %命令% | clip,,hide
; if RegExMatch(clipboard, "iO)([\w `t]+)[`r`n `t]+([^`r`n]+)", match)
; {
; m_First := match.Value(1)
; m_Second := match.Value(2)
; return % m_Second
; }
; }
; ; 方法三
; GetCpuID()
; {
; Version := StdoutToVar_CreateProcess("wmic cpu get Processorid")
; if RegExMatch(Version, "iO)([\w `t]+)[`r`n `t]+([^`r`n]+)", match)
; {
; m_First := match.Value(1)
; m_Second := match.Value(2)
; return % m_Second
; }
; }
; StdoutToVar_CreateProcess(sCmd, sEncoding:="CP858", sDir:="", ByRef nExitCode:=0) {
; DllCall( "CreatePipe", PtrP,hStdOutRd, PtrP,hStdOutWr, Ptr,0, UInt,0 )
; DllCall( "SetHandleInformation", Ptr,hStdOutWr, UInt,1, UInt,1 )

; VarSetCapacity( pi, (A_PtrSize == 4) ? 16 : 24, 0 )
; siSz := VarSetCapacity( si, (A_PtrSize == 4) ? 68 : 104, 0 )
; NumPut( siSz, si, 0, "UInt" )
; NumPut( 0x100, si, (A_PtrSize == 4) ? 44 : 60, "UInt" )
; NumPut( hStdInRd, si, (A_PtrSize == 4) ? 56 : 80, "Ptr" )
; NumPut( hStdOutWr, si, (A_PtrSize == 4) ? 60 : 88, "Ptr" )
; NumPut( hStdOutWr, si, (A_PtrSize == 4) ? 64 : 96, "Ptr" )

; if ( !DllCall( "CreateProcess", Ptr,0, Ptr,&sCmd, Ptr,0, Ptr,0, Int,True, UInt,0x08000000
; , Ptr,0, Ptr,sDir?&sDir:0, Ptr,&si, Ptr,&pi ) )
; return ""
; , DllCall( "CloseHandle", Ptr,hStdOutWr )
; , DllCall( "CloseHandle", Ptr,hStdOutRd )

; DllCall( "CloseHandle", Ptr,hStdOutWr ) ; The write pipe must be closed before Reading the stdout.
; VarSetCapacity(sTemp, 4095)
; while ( DllCall( "ReadFile", Ptr,hStdOutRd, Ptr,&sTemp, UInt,4095, PtrP,nSize, Ptr,0 ) )
; sOutput .= StrGet(&sTemp, nSize, sEncoding)

; DllCall( "GetExitCodeProcess", Ptr,NumGet(pi,0), UIntP,nExitCode )
; DllCall( "CloseHandle", Ptr,NumGet(pi,0) )
; DllCall( "CloseHandle", Ptr,NumGet(pi,A_PtrSize) )
; DllCall( "CloseHandle", Ptr,hStdOutRd )
; return sOutput
; }
```

## 获取当前电脑的名称，以及商品信息

```autohotkey
;http://msdn.microsoft.com/en-us/library/aa394105%28v=vs.85%29.aspx

str := "Caption,Description,IdentifyingNumber,Name,SKUNumber,UUID,Vendor,Version"
objWMIService := ComObjGet("winmgmts:{impersonationLevel=impersonate}!\\" . A_ComputerName . "\root\cimv2")
WQLQuery := "Select * From Win32_ComputerSystemProduct"
colSysProduct := objWMIService.ExecQuery(WQLQuery)._NewEnum
while colSysProduct[objSysProduct]
{
    loop Parse, % str,`,
        ProductInfo .= A_LoopField ": " objSysProduct[A_LoopField] "`n"
}
MsgBox % ProductInfo
```

## 网卡信息

```autohotkey
SwbemServices:= ComObjGet("Winmgmts:")
Nets := SwbemServices.ExecQuery("Select * from Win32_NetworkAdapter WHERE PhysicalAdapter ='TRUE'")
if(Nets.Count<0)
    Nets:=SwbemServices.ExecQuery("Select * from Win32_NetworkAdapter WHERE PNPDeviceID Like 'PCI%%' or PNPDeviceID Like 'USB%%'")
For Net In Nets
{
    If Net.NetConnectionStatus > 0
        str.= "网卡名称: " Net.Name "`n"
}

For Net In Nets
{
    If(Net.NetEnabled <>0)
        str1.= "网卡名称: " Net.Name "`n"
    else
        str2.="网卡名称: " Net.Name "`n"
}

MsgBox % "网卡共有如下:`n" str
MsgBox % "当前正在使用：`n" str1
MsgBox % "空闲：`n" str2
```

## BIOS信息

```autohotkey
strComputer := "."
objWMIService := ComObjGet("winmgmts:{impersonationLevel=impersonate}!\\" . strComputer . "\root\cimv2")
colSettings := objWMIService.ExecQuery("Select * from Win32_BIOS")._NewEnum
While colSettings[objBiosItem]
{
    MsgBox % "BIOSVersion : " . objBiosItem.BIOSVersion
    . "`nBuildNumber : " . objBiosItem.BuildNumber
    . "`nCaption : " . objBiosItem.Caption
    . "`nCurrentLanguage : " . objBiosItem.CurrentLanguage
    . "`nDescription : " . objBiosItem.Description
    . "`nInstallableLanguages : " . objBiosItem.InstallableLanguages
    . "`nInstallDate : " . objBiosItem.InstallDate
    . "`nListOfLanguages : " . objBiosItem.ListOfLanguages
    . "`nManufacturer : " . objBiosItem.Manufacturer
    . "`nName : " . objBiosItem.Name
    . "`nPrimaryBIOS : " . objBiosItem.PrimaryBIOS
    . "`nReleaseDate : " . objBiosItem.ReleaseDate
    . "`nSerialNumber2 : " . objBiosItem.SerialNumber
    . "`nSMBIOSBIOSVersion : " . objBiosItem.SMBIOSBIOSVersion
    . "`nSMBIOSMajorVersion : " . objBiosItem.SMBIOSMajorVersion
    . "`nSMBIOSMinorVersion : " . objBiosItem.SMBIOSMinorVersion
    . "`nSMBIOSPresent : " . objBiosItem.SMBIOSPresent
    . "`nSoftwareElementID : " . objBiosItem.SoftwareElementID
    . "`nSoftwareElementState : " . objBiosItem.SoftwareElementState
    . "`nStatus : " . objBiosItem.Status
    . "`nTargetOperatingSystem : " . objBiosItem.TargetOperatingSystem
    . "`nVersion : " . objBiosItem.Version
}
```

## CPU型号

```autohotkey
objWMIService:=ComObjGet("winmgmts:{impersonationLevel=impersonate}!\\.\root\cimv2")
msgbox % Win32_Processor(objWMIService,SystemCPU)

Win32_Processor(o,ByRef SystemCPU) {
    colItems := o.ExecQuery("SELECT * FROM Win32_Processor")._NewEnum
    while colItems[objItem]
        return SystemCPU:=RegExReplace(objItem.Name,"(\s{2,}|\t)"," ")
}
```
