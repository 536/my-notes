# pdf转word

<https://github.com/dothinking/pdf2docx>

```python
# pip install pdf2docx
from pathlib import Path

from pdf2docx import Converter
pdf_name = Path(__file__).parent / 'XXX.pdf'
docx_named = pdf_name.with_suffix('.docx')

cv = Converter(pdf_name.as_posix())
cv.convert(docx_named.as_posix())
cv.close()
```
