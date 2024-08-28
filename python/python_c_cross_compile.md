distutils模块
There are three possible config files: distutils.cfg in the
Distutils installation directory (ie. where the top-level
Distutils __inst__.py file lives), a file in the user's home
directory named .pydistutils.cfg on Unix and pydistutils.cfg
on Windows/Mac; and setup.cfg in the current directory.

无distutils.cfg需新建
[build]
compiler=mingw32

[build_ext]
compiler=mingw32