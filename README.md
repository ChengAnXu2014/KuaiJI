# KuaiJi
一个可以帮助你快速查阅笔记的 ***Sublime Text 3*** 插件。
当笔记文件内容太多太杂时，查阅笔记会是一件非常麻烦的事情。本插件可以让你方便地在笔记的不同段落之间跳转，比在查阅某些官方在线文档时通过链接跳转还要方便得多。还支持用不同的颜色和字体样式化显示标题、批注等特殊内容，让阅读更方便。


## 下载和安装
1. 下载：  
点击右上的橙色大按钮**Clone or download**,在弹出的下拉菜单中点击最下方的**Download ZIP**
2. 安装：  
解压下载的ZIP文件，你会得到一个名为*KuaiJi*的文件夹；  
在***Sublime Text 3***中通过菜单**Preferences => Browse Packages**打开*Packages*目录；  
把*KuaiJi*文件夹复制到*Packages*目录下就可以了。

## 功能
本插件通过`<<>>`识别*标题*，在一个快捷面板中列出当前文档中所有的*标题*。当用户选中某个*标题*时，文档会自动跳转到该*标题*所在位置(*标题*在正中央)，并会用显眼的颜色高亮显示*标题*。


## 设置
本插件有两个设置项：  
```
'kuaiji_title_prefix': '<<',  
'kuaiji_title_sufix': '>>'  
```
分别指定了*标题*前缀和*标题*后缀  


## 命令
本插件只有一个命令：  
`find_in_file`  
也就是驼峰模式下的：  
`FindInFile`  


## 用法
在使用本插件之前，要先做一些准备工作：  
1. 打开***Sublime Text 3***，通过菜单**Preferences => Color Scheme**启用*mariana*主题。  
2. 新建一个文件，把下面提供的内容复制进去，并将其保存为*View.pkj*。  
3. 通过菜单**KuaiJi => Find In File**或快捷键`alt+m`调用本插件。  
-----
你会看到一个快捷面板中列出了*View.pkj*中所有的*标题*，随便点击一个*标题*条目，文档就会自动跳转到该*标题*所在位置。


## 语法和扩展名
1. 为了让笔记内容看起来更有条理，本插件定义了一些简单的样式化文本语法。在下面给出的*view.pkj*内容的开头给出了直观的例子，一看就懂。  
2. 本插件的初衷是作者为了方便查阅自学编程所作的笔记而写。为了使笔记中出现的代码和关键字能支持对应编程语言的样式化显示，定义了以下扩展名：  
.kj:只支持单纯的*KuaiJi*语法。
.pkj:除了*KuaiJi*语法外，还支持*Phthon*语法。
.skj:除了*KuaiJi*语法外，还支持*shell*语法。
.jkj:除了*KuaiJi*语法外，还支持*JSON, js*语法。
.ykj:除了*KuaiJi*语法外，还支持*YAML*语法。


## *View.pkj*内容
```
<<这是一个标题>>
 这是一个小标题:
ps:这是一个批注
我是`这是一条行内斜体文本`天才
我是 `这是一条行内粗体文本`天才
我是 `这是一条行内粗斜体文本` 天才



 The methods of Sublime.View Class:



ps:Try shortcut:"alt+m", you will see a quick panel with titiles list, select a title, you can jump to the content of the selected title in this view.

ps:You can also do this with the main menu: KuaiJi => Find In File

<<id()>>
 int:
Returns a number that uniquely identifies this view.



<<buffer_id()>>
 int:
Returns a number that uniquely identifies the buffer underlying this view.



<<is_primary()>>
 bool:
If the view is the primary view into a file. Will only be False if the user has opened multiple views into a file.



<<file_name()>>
 str:
The full name file the file associated with the buffer, or None if it doesn't exist on disk.



<<name()>>
 str:
The name assigned to the buffer, if any



<<set_name(name)>>
 None:
Assigns a name to the buffer



<<is_loading()>>
 bool:
Returns True if the buffer is still loading from disk, and not ready for use.



<<is_dirty()>>
 bool:
Returns True if there are any unsaved modifications to the buffer.



<<is_read_only()>>
 bool:
Returns True if the buffer may not be modified.



<<set_read_only(value)>>
 None:
Sets the read only property on the buffer.



<<is_scratch()>>
 bool:
Returns True if the buffer is a scratch buffer. Scratch buffers never report as being dirty.



<<set_scratch(value)>>
 None:
Sets the scratch property on the buffer.



<<settings()>>
 Settings:
Returns a reference to the view's settings object. Any changes to this settings object will be private to this view.



<<window()>>
 Window:
Returns a reference to the window containing the view.



<<run_command(string, <args>)>>
 None:
Runs the named TextCommand with the (optional) given args.



<<size()>>
 int:
Returns the number of character in the file.



<<substr(region)>>
 str:
Returns the contents of the region as a string.



<<substr(point)>>
 str:
Returns the character to the right of the point.



<<insert(edit, point, string)>>
 int:
Inserts the given string in the buffer at the specified point. Returns the number of characters inserted: this may be different if tabs are being translated into spaces in the current buffer.



<<erase(edit, region)>>
 None:
Erases the contents of the region from the buffer.



<<replace(edit, region, string)>>
 None:
Replaces the contents of the region with the given string.



<<sel()>>
 Selection:
Returns a reference to the selection.



<<line(point)>>
 Region:
Returns the line that contains the point.



<<line(region)>>
 Region:
Returns a modified copy of region such that it starts at the beginning of a line, and ends at the end of a line. Note that it may span several lines.



<<full_line(point)>>
 Region:
As line(), but the region includes the trailing newline character, if any.



<<full_line(region)>>
 Region:
As line(), but the region includes the trailing newline character, if any.



<<lines(region)>>
[Region] 	Returns a list of lines (in sorted order) intersecting the region.



<<split_by_newlines(region)>>
[Region] 	Splits the region up such that each region returned exists on exactly one line.



<<word(point)>>
 Region:
Returns the word that contains the point.



<<word(region)>>
 Region:
Returns a modified copy of region such that it starts at the beginning of a word, and ends at the end of a word. Note that it may span several words.



<<classify(point)>>
 int:


Classifies point, returning a bitwise OR of zero or more of these flags:

    sublime.CLASS_WORD_START
    sublime.CLASS_WORD_END
    sublime.CLASS_PUNCTUATION_START
    sublime.CLASS_PUNCTUATION_END
    sublime.CLASS_SUB_WORD_START
    sublime.CLASS_SUB_WORD_END
    sublime.CLASS_LINE_START
    sublime.CLASS_LINE_END
    sublime.CLASS_EMPTY_LINE




<<find_by_class(point, forward, classes, <separators>)>>
 Region:
Finds the next location after point that matches the given classes. If forward is False, searches backwards instead of forwards. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.



<<expand_by_class(point, classes, <separators>)>>
 Region:
Expands point to the left and right, until each side lands on a location that matches classes. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.



<<expand_by_class(region, classes, <separators>)>>
 Region:
Expands region to the left and right, until each side lands on a location that matches classes. classes is a bitwise OR of the sublime.CLASS_XXX flags. separators may be passed in, to define what characters should be considered to separate words.



<<find(pattern, start_point, <flags>)>>
 Region:
Returns the first region matching the regex pattern, starting from start_point, or None if it can't be found. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together.



<<find_all(pattern, <flags>, <format>, <extractions>)>>
[Region] 	Returns all (non-overlapping) regions matching the regex pattern. The optional flags parameter may be sublime.LITERAL, sublime.IGNORECASE, or the two ORed together. If a format string is given, then all matches will be formatted with the formatted string and placed into the extractions list.



<<rowcol(point)>>
(int, int) 	Calculates the 0-based line and column numbers of the point.



<<text_point(row, col)>>
 int:
Calculates the character offset of the given, 0-based, row and col. Note that col is interpreted as the number of characters to advance past the beginning of the row.



<<set_syntax_file(syntax_file)>>
 None:
Changes the syntax used by the view. syntax_file should be a name along the lines of Packages/Python/Python.tmLanguage. To retrieve the current syntax, use view.settings().get('syntax').



<<extract_scope(point)>>
 Region:
Returns the extent of the syntax scope name assigned to the character at the given point.



<<scope_name(point)>>
 str:
Returns the syntax scope name assigned to the character at the given point.



<<match_selector(point, selector)>>
 bool:
Checks the selector against the scope at the given point, returning a bool if they match.



<<score_selector(point, selector)>>
 int:
Matches the selector against the scope at the given point, returning a score. A score of 0 means no match, above 0 means a match. Different selectors may be compared against the same scope: a higher score means the selector is a better match for the scope.



<<find_by_selector(selector)>>
[Region] 	Finds all regions in the file matching the given selector, returning them as a list.



<<show(location, <show_surrounds>)>>
 None:
Scroll the view to show the given location, which may be a point, Region or Selection.



<<show_at_center(location)>>
 None:
Scroll the view to center on the location, which may be a point or Region.



<<visible_region()>>
 Region:
Returns the currently visible area of the view.



<<viewport_position()>>
 vector:
Returns the offset of the viewport in layout coordinates.



<<set_viewport_position(vector, <animate<)>>
 None:
Scrolls the viewport to the given layout position.



<<viewport_extent()>>
 vector:
Returns the width and height of the viewport.



<<layout_extent()>>
 vector:
Returns the width and height of the layout.



<<text_to_layout(point)>>
 vector:
Converts a text point to a layout position



<<text_to_window(point)>>
 vector:
Converts a text point to a window position



<<layout_to_text(vector)>>
 point:
Converts a layout position to a text point



<<layout_to_window(vector)>>
 vector:
Converts a layout position to a window position



<<window_to_layout(vector)>>
 vector:
Converts a window position to a layout position



<<window_to_text(vector)>>
 point:
Converts a window position to a text point



<<line_height()>>
 dip:
Returns the light height used in the layout



<<em_width()>>
 dip:
Returns the typical character width used in the layout



<<add_regions(key, [regions], <scope>, <icon>, <flags>)>>
 None:


Add a set of regions to the view. If a set of regions already exists with the given key, they will be overwritten. The scope is used to source a color to draw the regions in, it should be the name of a scope, such as "comment" or "string". If the scope is empty, the regions won't be drawn.

The optional icon name, if given, will draw the named icons in the gutter next to each region. The icon will be tinted using the color associated with the scope. Valid icon names are dot, circle and bookmark. The icon name may also be a full package relative path, such as Packages/Theme - Default/dot.png.

The optional flags parameter is a bitwise combination of:

    sublime.DRAW_EMPTY: Draw empty regions with a vertical bar. By default, they aren't drawn at all.
    sublime.HIDE_ON_MINIMAP: Don't show the regions on the minimap.
    sublime.DRAW_EMPTY_AS_OVERWRITE: Draw empty regions with a horizontal bar instead of a vertical one.
    sublime.DRAW_NO_FILL: Disable filling the regions, leaving only the outline.
    sublime.DRAW_NO_OUTLINE: Disable drawing the outline of the regions.
    sublime.DRAW_SOLID_UNDERLINE: Draw a solid underline below the regions.
    sublime.DRAW_STIPPLED_UNDERLINE: Draw a stippled underline below the regions.
    sublime.DRAW_SQUIGGLY_UNDERLINE: Draw a squiggly underline below the regions.
    sublime.PERSISTENT: Save the regions in the session.
    sublime.HIDDEN: Don't draw the regions.

The underline styles are exclusive, either zero or one of them should be given. If using an underline, sublime.DRAW_NO_FILL and sublime.DRAW_NO_OUTLINE should generally be passed in.



<<get_regions(key)>>
[Region] 	Return the regions associated with the given key, if any



<<erase_regions(key)>>
 None:
Removed the named regions



<<set_status(key, value)>>
 None:
Adds the status key to the view. The value will be displayed in the status bar, in a comma separated list of all status values, ordered by key. Setting the value to the empty string will clear the status.



<<get_status(key)>>
 str:
Returns the previously assigned value associated with the key, if any.



<<erase_status(key)>>
 None:
Clears the named status.



<<command_history(index, <modifying_only>)>>
(str, dict, int) 	

Returns the command name, command arguments, and repeat count for the given history entry, as stored in the undo / redo stack.

Index 0 corresponds to the most recent command, -1 the command before that, and so on. Positive values for index indicate to look in the redo stack for commands. If the undo / redo history doesn't extend far enough, then (None, None, 0) will be returned.

Setting modifying_only to True (the default is False) will only return entries that modified the buffer.



<<change_count()>>
 int:
Returns the current change count. Each time the buffer is modified, the change count is incremented. The change count can be used to determine if the buffer has changed since the last it was inspected.



<<fold([regions])>>
 bool:
Folds the given regions, returning False if they were already folded



<<fold(region)>>
 bool:
Folds the given region, returning False if it was already folded



<<unfold(region)>>
[Region] 	Unfolds all text in the region, returning the unfolded regions



<<unfold([regions])>>
[Region] 	Unfolds all text in the regions, returning the unfolded regions



<<encoding()>>
 str:
Returns the encoding currently associated with the file



<<set_encoding(encoding)>>
 None:
Applies a new encoding to the file. This encoding will be used the next time the file is saved.



<<line_endings()>>
 str:
Returns the line endings used by the current file.



<<set_line_endings(line_endings)>>
 None:
Sets the line endings that will be applied when next saving.



<<overwrite_status()>>
 bool:
Returns the overwrite status, which the user normally toggles via the insert key.



<<set_overwrite_status(enabled)>>
 None:
Sets the overwrite status.



<<symbols()>>
[(Region, str)] 	Extract all the symbols defined in the buffer.



<<show_popup_menu(items, on_done, <flags>)>>
 None:


Shows a pop up menu at the caret, to select an item in a list. on_done will be called once, with the index of the selected item. If the pop up menu was cancelled, on_done will be called with an argument of -1.

items is a list of strings.

flags it currently unused.



<<show_popup(content, <flags>, <location>, <max_width>, <max_height>, <on_navigate>, <on_hide>)>>
 None:


Shows a popup displaying HTML content.

flags is a bitwise combination of the following:

    sublime.COOPERATE_WITH_AUTO_COMPLETE. Causes the popup to display next to the auto complete menu
    sublime.HIDE_ON_MOUSE_MOVE. Causes the popup to hide when the mouse is moved, clicked or scrolled
    sublime.HIDE_ON_MOUSE_MOVE_AWAY. Causes the popup to hide when the mouse is moved (unless towards the popup), or when clicked or scrolled

The default location of -1 will display the popup at the cursor, otherwise a text point should be passed.

max_width and max_height set the maximum dimensions for the popup, after which scroll bars will be displayed.

on_navigate is a callback that should accept a string contents of the href attribute on the link the user clicked.

on_hide is called when the popup is hidden.



<<update_popup(content)>>
 None:
Updates the contents of the currently visible popup.



<<is_popup_visible()>>
 bool:
Returns if the popup is currently shown.



<<hide_popup()>>
 None:
Hides the popup.



<<is_auto_complete_visible()>>
 bool:
Returns if the auto complete menu is currently visible.



<<style()>>
 dict:
Returns a dict of the global style settings for the view. All colors are normalized to the six character hex form with a leading hash, e.g. #ff0000.



<<style_for_scope(scope_name)>>
 dict:
Accepts a string scope name and returns a dict of style information, include the keys foreground, bold, italic, source_line, source_column and source_file. If the scope has a background color set, the key background will be present. The foreground and background colors are normalized to the six character hex form with a leading hash, e.g. #ff0000.



<<set_reference_document(reference)>>
 None:
Uses the string reference to calculate the initial diff for the incremental diff



<<reset_reference_document()>>
 None:
Clears the state of the incremental diff for the view 
```