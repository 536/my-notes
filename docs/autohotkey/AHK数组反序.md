# AHK数组反序

```autohotkey
;https://blog.csdn.net/liuyukuan/article/details/85158771
;作者：sunwind
;2018年12月21日
;功能：数组反转顺序输出

arr := ["a", "b", "c"]
Msgbox, % arr.join("|")
Msgbox, % arr.reverse().join("`n")
return

Array(p*){
    p.base := Object("join", "Array_Join", "reverse", "Array_Reverse")
    Return p
}
Array_Reverse(arr) {
    arr2 := Array()
    Loop, % len:=arr.maxindex()
    {
        arr2[len-(A_Index-1)] := arr[A_Index]
    }
    Return arr2
}

Array_Join(this, sep="`n"){
    ;~ MsgBox % "Array_Join arr[1]: " . this[1]
    Loop, % this.maxindex()
        str .= this[A_Index] sep
    StringTrimRight, str, str, % StrLen(sep)
    return str
}
```
