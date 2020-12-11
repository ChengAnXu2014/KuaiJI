# KuaiJi
一个可以帮助你快速查阅笔记的 ***Sublime Text 3*** 插件。
当笔记文件内容太多太杂时，查阅笔记会是一件非常麻烦的事情。本插件可以让你方便地在笔记的不同段落之间跳转，比在查阅某些官方在线文档时通过链接跳转还要方便得多。还支持用不同的颜色和字体样式化显示*标题*、批注等特殊内容，让阅读更方便。


## 下载和安装
1. 下载：  
点击右上的橙色大按钮**Clone or download**,在弹出的下拉菜单中点击最下方的**Download ZIP**
2. 安装：  
解压下载的ZIP文件，你会得到一个名为*KuaiJi*的文件夹；  
在***Sublime Text 3***中通过菜单**Preferences => Browse Packages**打开*Packages*目录；  
把*KuaiJi*文件夹复制到*Packages*目录下就可以了。
3. *KuaiJi*文件夹中有一个*笔记*文件夹，里面保存的是示例笔记文件，把*笔记*文件夹剪切到你喜欢的目录下，在下面介绍**用法**时会用到。

## 功能
本插件通过`正则表达式`识别*标题*，在一个快捷面板中列出当前文档中所有的*标题*。当用户选中某个*标题*时，文档会自动跳转到该*标题*所在位置(*标题*在正中央)。


## 命令
本插件只有一个命令：  
`find_in_file`  
也就是驼峰模式下的：  
`FindInFile`  


## 用法
在使用本插件之前，要先做一些准备工作：  
1. 打开***Sublime Text 3***，通过菜单**Preferences => Color Scheme**启用*mariana*主题。  
2. 打开你下载的*KuaiJi*文件夹内的*笔记*文件夹，用***Sublime Text 3***打开其中的任意一个文件。  
3. 通过菜单**KuaiJi => Find In File**或快捷键`alt+m`调用本插件。  
-----
你会看到一个快捷面板中列出了你打开的笔记示例文件中所有的*标题*，非顶级的*标题*下还会有一行小字标出它所属的上级*标题*；随便点击一个*标题*条目，文档就会自动跳转到该*标题*所在位置。


## 语法和扩展名
### 标题识别
v1.1.0以上版本的*快记*采用分级*标题*，*标题*独占一行，以1至无数多个英文小数点开始，以英文冒号结尾。顶级*标题*为:`.标题:`，二级*标题*为:`..标题:`，以此类推，前面带几个小数点就代表是几级*标题*。  
理论上可以有无数多级*标题*，但是只有前五级*标题*会高亮显示。  


### 样式化内容
为了让笔记内容看起来更有条理，本插件定义了一些简单的样式化文本语法：  
1. ` 小标签:`位于行首，以1至5个空格开头，以英文冒号结尾。采用该格式的文本会高亮显示，以便于识别。注意，冒号是英文半角的。用法如下例：  
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
2. `!:强调内容!`:可位于文本的任何位置，以英文感叹号加冒号开始，以另一个英文感叹号结尾；会用十分扎眼的颜色高亮显示，可用于文本中需要特别强调的部分。  


### 源代码样式化显示
本插件的初衷是作者为了方便查阅自学编程所作的笔记而写。  
为了使笔记中出现的代码和关键字能使用***Sublime Text 3***默认的对各种编程语言源代码的样式化显示，本插件提供了以下两种方式：  
1. 通过扩展名为整个笔记文件指定编程语言：  
.kj:只支持单纯的*KuaiJi*语法。  
.ckj:除了*KuaiJi*语法外，还支持*C/C++*语法。  
.cskj:除了*KuaiJi*语法外，还支持*CSS*语法。  
.hkj:除了*KuaiJi*语法外，还支持*HTML*语法。  
.jkj:除了*KuaiJi*语法外，还支持*JSON/js*语法。  
.pkj:除了*KuaiJi*语法外，还支持*Phthon*语法。  
.skj:除了*KuaiJi*语法外，还支持*shell*语法。  
.ykj:除了*KuaiJi*语法外，还支持*YAML*语法。  

2. 为笔记中的某个段落指定编程语言：  
*C/C++*:  
```
`c
# include<stdio.h>
int main(void)
{
	printf("hello world");
	return 0;
}
`
```
*CSS*:  
```
`cs
.clsContainer
{
	background: #ff0000;
}
`
```
*HTML*  
```
`hl
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

</body>
</html>
`
```
*JavaScript*:  
```
`js
var name="Aoi Sola";
`
```
*Python*:  
```
`py
import os
print("hello world")
`
```
*Shell*  
```
`sh
echo 'hellow world'
`
```
*YAML*  
```
`yl
- match: '^`cs$\n'
  scope: code.hr.kj
  embed: Packages/CSS/CSS.sublime-syntax
  escape: '^`$\n'
  escape_captures:
    0: code.hr.kj
`
```