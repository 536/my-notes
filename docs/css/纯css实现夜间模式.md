# 纯css实现夜间模式

## 使用

如果是个人开发的网站，添加以下css即可

```css
@media (prefers-color-scheme: dark) {
    html {
        background: #FFF !important;
        filter: invert(0.88) hue-rotate(180deg) !important;
    }
    video,
    img {
        filter: invert(1) hue-rotate(180deg) !important;
    }
}
```

对于其他网站，需要安装浏览器插件[`xStyle`](https://github.com/FirefoxBar/xStyle)/`stylish`之类的插件，以`xStyle`为例

添加以下样式

```css
@-moz-document exclude("^.*github.com.*$"),
exclude("^.*github.com.*$"),
exclude("^.*google.com.*$"),
exclude("^.*sspai.com.*$"),
exclude("^.*youtube.com.*$") {
    @media (prefers-color-scheme: dark) {
        html {
            background: #FFF !important;
            filter: invert(0.88) hue-rotate(180deg) !important;
        }
        video,
        img {
            filter: invert(1) hue-rotate(180deg) !important;
        }
    }
}
```

## 原理

1. css `filter`属性实现夜间模式

   1. 页面颜色值翻转
   2. 图片、视频取消翻转

   <https://www.zhangxinxu.com/wordpress/2020/11/css-mix-blend-mode-filter-dark-theme/>

2. css `media`-`prefers-color-scheme`属性介绍

   将用户自定义的系统夜间模式属性值，作为`media`接口传递给css

   <https://developer.mozilla.org/zh-CN/docs/Web/CSS/@media/prefers-color-scheme>

3. `xStyle`的`exclude`匹配格式

   排除已适配夜间模式的网站，比如`github.com`/`google.com`等

   <https://github.com/FirefoxBar/xStyle/wiki/样式格式#exclude>
