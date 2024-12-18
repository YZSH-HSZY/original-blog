[TOC]

# pelican
pelican是python实现的静态网站生成器。

[pelican官方文档](https://docs.getpelican.com/zh-cn/stable/quickstart.html)

## 安装

- 使用pip安装pelican包 `pip install pelican`
**注意** pelican需要python>=3.8.1
- 添加markdown扩展 `pip install "pelican[markdown]"`
- 添加排版增强 `pip install typogrify`, 之后可在设置文件中启用

> pelican安装后主要包含如下依赖:
```python
feedgenerator，用于生成Atom feeds
jinja2，用于模板系统
pygments，用于语法高亮
docutils，用于reStructuredText格式
blinker，对象-对象的信号广播系统
unidecode，用于将Unicode文本转为ASCII字符的音译
MarkupSafe，用于转义字符的安全处理
python-dateutil，用于读取日期相关的元数据
```

## 专有术语

### 文章(Articles)和页面(pages)
pelican将文章(article)视为有时间顺序的内容，界面(page)指不经常改变的内容

### 文件元数据(File metadata)
pelican可以从文件系统中自动地获取一些信息（例如文章的分类），但是对与有些信息需要以元数据的形式在文件中提供
> rst格式元信息如下:
```rs
My super title
##############

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds
```
> markdown格式元信息如下:
```markdown
---
Title: My super title
Date: 2010-12-03 10:20
---

This is the content of my super blog post.
```

* pelican所有内置支持的matedata如下:

|元数据类型       |描述                                                     |
|----------------|---------------------------------------------------------|
|title           |文章或页面的标题                                          |
|date            |发布日期（需要以 YYYY-MM-DD HH:SS 的格式）                 |
|modified        |最后修改日期（需要以 YYYY-MM-DD HH:SS 的格式），未指定自动与date一致             |
|tags            |推文标签，以逗号分隔                                       |
|keywords        |推文关键字，以逗号分隔（只能在HTML内容中使用）               |
|category        |推文分类（只能归属到一个分类中，不支持多个）                 |
|slug            |URL和翻译的唯一标识符                                     |
|author          |当只有一个作者时可以使用这个元数据                          |
|authors         |当有多个作者时需要使用这个元数据(以`,`分隔多个作者)                        |
|summary         |简短的推文概要，会显示在首页上                              |
|lang            |推文所用语言的ID（例如 en 、 fr 、 zh-cn 等）               |
|translation     |手动指定当前内容是否是某个翻译版本（该元数据的值只能是 true 或 false）|
|status          |推文的状态： draft、 hidden 、 skip 或 published            |
|template        |用于指定要使用的生成模板，只需要写模板的名字，不需要模板文件的后缀名|
|save_as         |将内容保存到指定的相对文件路径                                |
|url             |指定本篇文章或页面要使用的URL                                 |

**注意1** slug可以通过元数据手动指定，若没有，Pelican会根据文章的标题（title）来自动生成slug。
**注意2** 标题是唯一必须指定的元数据，可在设置中添加 `FILENAME_METADATA = '(?P<title>.*)'` ，此时pelican会自动将文件名作为内容的标题。

### 内部链接(Linking to internal content)
pelican 3.1开始，站内链接可以在 源文件 层次下指定，而不是只能在 生成后的站点 层次下指定。

- md中内部链接的格式为 `{filename}path/to/file`(相对于当前文件) 或 `{filename}/path/file`(相对于content root)

**注意** 路径的分隔符均使用 `/`

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

### 简易使用

借助 `pelican-quickstart` 创建一个项目架构

> 项目骨架如下
```
project_dir/
├── content
│   └── (pages)          # 存放不需要按时间排序的内容
├── output
├── tasks.py
├── Makefile
├── pelicanconf.py       # 主设置文件
└── publishconf.py       # 发布时的设置
```

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