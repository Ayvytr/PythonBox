# PythonBox

# 常用库链接：

清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/



### pip 





WARNING: The repository located at mirrors.aliyun.com is not a trusted or secure host and is being ignored. If this repository is available via HTTPS we recommend you use HTTPS instead, otherwise you may silence this warning and allow it anyway with '--trusted-host mirrors.aliyun.com'.



pip install -i http://mirrors.aliyun.com/pypi/simple/ pyqt5Designer --trusted-host mirrors.aliyun.com





python -m pip install --upgrade pip



### pyinstall

TypeError: an integer is required (got type bytes)

解决办法：报错前的pyinstaller是用 pip install pyinstaller 来安装的，改成用 pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz 再安装一次





## Pycharm PyQt



```
QtDesigner

Working Directory: $FileDir$


PyUIC
Program:python.exe
Arguments: -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
Working Directory: $FileDir$

PyRcc
Program: Scripts\pyrcc5.exe
Arguments: $FileName$ -o $FileNameWithoutExtension$.py 
Working Directory: $FileDir$

```