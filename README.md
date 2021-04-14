# 下面有中文介绍

## Why is KuaiJi useful?
*KuaiJi* can help developers to read and refer their note files more easily.  
*KuaiJi* use *regex* to find *titles* in current *view*, show *titles* in a *quick panel*.  
When users click a *title*, current *view* will scroll to make the chosen *title* in the center of the *view port*.  
To make the *titles* more easier to find, *KuaiJi* use scope `invalid.illegal` to set their background to red.  
To use the style of *KuaiJi* syntax, you must change your note file's extension name to `.kj`.


## What is a *title*?
*title* must match the *regex* `^\.+[^.].*:$`.  
Which means, *title* is a line started with one or more `.`s, and ended with a `:`.  
Such as:  
```
.Methods of Sublime Module:
..version():
..platform():
..arch():
```
The *title*s with one `.` are top-level *title*s, the *title*s with two `.`s are second-level *title*s, and so on.
The non-top-level *title*s in the *quick panel*, will have their suplevel *title*s followed next line.



## How to use *KuaiJi*?
Open a file named `*.kj`, which contain *title*s in it.  
Use **AnXu => Kuaiji Find** menu or `alt+m` shortcut to invoke the *quick panel*.  
Then click one of the *title*s shown in the *quick panel*, current *view* will scroll to make the chosen *title* in the center of the *view port*


## Customization
The command binded to **AnXu => Kuaiji Find** menu and `alt+m` shortcut is `kuaiji_find`,
 or in *camel mode* `KuaijiFind`.  
You can use it to customize the menu and shortcut.


## Special words
*KuaiJi* use **sublime-syntax** to make the special words in the note files colorful.  
The special words include but not limited to:  
Key words of language *C*, e.g. `if else char int float` etc;  
Key words of script *Python*, e.g. `self list dict tuple set bytes bytearray` etc;  
Key words of other program languages;  
Other special words like language names, e.g. `XML HTML YAML Python Json JS ` etc.



# KuaiJi
一个可以帮助你快速查阅笔记的 ***Sublime Text 3*** 插件。
当笔记文件内容太多太杂时，查阅笔记会是一件非常麻烦的事情。  
本插件可以让你方便地在笔记的不同段落之间跳转，还支持用不同的颜色和字体样式化显示*标题*、批注等特殊内容，让阅读更方便。


## 下载和安装
1. 下载：  
点击右上的橙色大按钮英文模式下为**Clone or download**中文模式下为**克隆/下载**,在弹出的下拉菜单中点击最下方的下载按钮英文模式下为**Download ZIP**中文模式下为**下载ZIP**  
2. 安装：  
解压下载的ZIP文件，你会得到一个名为*KuaiJi*的文件夹；  
在***Sublime Text 3***中通过菜单**Preferences => Browse Packages**打开*Packages*目录；  
把*KuaiJi*文件夹复制到*Packages*目录下就可以了。
3. 我的另一个库*笔记*里有我所有的学习笔记文件，你可以参考这些笔记内容的格式来编辑你自己的笔记文件。  
*KuaiJi*文件夹中还有个名为*SublimeText3*的文件夹，里面是***Sublime Text 3***安装包和*Package Conthrol*等插件包。***Sublime Text 3***安装包中包含了适用于Windows系统32位和64位的两个版本。  
还没有安装***Sublime Text 3***的朋友可以直接安装，不用再去官网下载了，官网下载实在是太慢了。

## 功能
本插件通过`正则表达式`识别*标题*，在一个快捷面板中列出当前文档中所有的*标题*。当用户选中某个*标题*时，文档会自动跳转到该*标题*所在位置(*标题*在正中央)。


## 命令
本插件只有一个命令：  
`kuaiji_find`  
也就是驼峰模式下的：  
`KuaijiFind`  


## 用法
在使用本插件之前，要先做一些准备工作：  
1. 新建一个文本文件夹，并将其改名为`test.kj`。  
2. 在***Sublime Text 3***中打开它，将我的另一个库*笔记*中的笔记文件`SublimeText/Usage.kj`的内容复制到`test.kj`中。  
3. 通过菜单**AnXu => Kuaiji Find**或快捷键`alt+m`调用本插件。  
-----
你会看到一个快捷面板中列出了`test.kj`文件中所有的*标题*，非顶级的*标题*下还会有一行小字标出它所属的上级*标题*；随便点击一个*标题*条目，文档就会自动跳转到该*标题*所在位置。


## 语法和扩展名
### 标题识别
v1.1.0以上版本的*快记*采用分级*标题*，*标题*独占一行，以1至无数多个英文小数点开始，以英文冒号结尾。  
顶级*标题*为:`.标题:`，二级*标题*为:`..标题:`，以此类推，前面带几个小数点就代表是几级*标题*。  
所有标题都会用显眼的颜色高亮显示，并且可以通过**用法**中介绍的方法快速跳转。  


### 样式化内容
为了让笔记内容看起来更有条理，本插件定义了一些简单的样式化文本语法：  
1. ` 小标题:`  
独占一行，以空格开头，以英文冒号结尾。采用该格式的文本会高亮显示，以便于识别，但是无法快速跳转。  
注意，冒号是英文半角的。用法如下例：  
*Python*`print()`函数的详解：  
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
 参数:
  objects: .....
  sep: .....
  end: .....
  file: .....
  flush: .....
 返回值: ....
 描述: .....
```
2. `-表头:`  
独占一行，以`-`开头，以英文冒号结尾。*表头*除本身会高亮显示外，还标志着其后所跟连续非空行为列表。  
`列表条目:`*表头*后所跟的连续非空行中，以空格开头以英文冒号结尾的最短文本。例如：
*Python*`print()`函数的详解：  
```
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
-参数:
  objects: .....
  sep: .....
  end: .....
  file: .....
  flush: .....

返回值:....

描述:.....
```


### 扩展名
适用于本插件的笔记文件要采用`.kj`扩展名。
