# pelican
pelican是python实现的静态网站生成器。

[pelican官方文档](https://docs.getpelican.com/zh-cn/stable/quickstart.html)

## 专有术语

## 设置文件`pelicanconf.py`
```python

ARTICLE_URL = '{slug}.html'  # 文章的 URL
ARTICLE_SAVE_AS = '{slug}.html'  # 文章保存的地方

ARTICLE_LANG_URL = '{slug}-{lang}.html'  # 不使用默认语言的文章的URL指向
ARTICLE_LANG_SAVE_AS = '{slug}-{lang}.html'  # 将保存不使用默认语言的文章的位置

DRAFT_URL = 'drafts/{slug}.html'  # 引用文章草稿的 URL
DRAFT_SAVE_AS = 'drafts/{slug}.html'  # 保存文章草稿的地方

PAGE_URL = 'pages/{slug}.html'  # 链接到页面的 URL
PAGE_SAVE_AS = 'pages/{slug}.html'  # 保存页面的位置。这个值必须与 PAGE_URL 相同，或者在服务器配置中使用重写
```

## 示例

### 更改编写的md文件生成的html文件名

pelican是多线程的，因此在代码查看和处调试时，不太方便，需要你根据源码推测断点位置。
在pelican/writers.py::write_file 断点，可以输出文件名从上层的article.save_as获取，为Content的属性save_as，获取时可以覆写，参下:
```python
class Content:
    @property
    def save_as(self) -> str:
        return self.get_url_setting("save_as")
    
    def get_url_setting(self, key: str) -> str:
        if hasattr(self, "override_" + key):
            return getattr(self, "override_" + key)
        key = key if self.in_default_lang else f"lang_{key}"
        return self._expand_settings(key)
```
可通过更改配置项 `ARTICLE_URL`/`ARTICLE_SAVE_AS`/`PAGE_URL`/`PAGE_SAVE_AS` 来更改输出html位置和文件名及主页的链接