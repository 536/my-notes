# AHK通过COM创建Word文件

```autohotkey
Word := ComObjCreate("Word.Application")
Doc := Word.Documents.Add
Doc.SaveAs(A_Desktop "\" A_Now ".doc")
Word.Quit
```
