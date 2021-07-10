# python转换markdown为HTML及代码高亮

## mistune库

`$ pip install mistune==2.0.0rc1`

+ 转换

```python
from pygments import highlight
from pygments.formatters import html
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound


# 先自定义代码高亮的解析器，继承自内置的HTMLRenderer
class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
            except ClassNotFound:
                lexer = get_lexer_by_name('text', stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return '<pre><code>' + mistune.escape(code) + '</code></pre>'


# 创建解析器，renderer定义为上面自定义的解析器
markdown = mistune.create_markdown(renderer=HighlightRenderer(), escape=True)
# 将markdown内容转换成html内容
html_content = markdown(md_content)
```

+ 生成css

    ```text
    $ pygmentize -f html -a .highlight -S default > highlight.css

    -a .highlight 指定共同祖先class

    -S default 指定样式名称（default）
    ```

+ 合并

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>index</title>
        <link href="highlight.css" rel="stylesheet">
    </head>
    <body>
        %s
    </body>
    </html>
    ```

## markdown库

未作深入研究
