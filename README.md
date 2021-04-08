# Why is KuaiJi useful?
*KuaiJi* can help developers to read and refer their note files more easily.  
*KuaiJi* use *regex* to find *titles* in current *view*, show *titles* in a *quick panel*.  
When users click a *title*, current *view* will scroll to make the chosen *title* in the center of the *view port*.  
To make the *titles* more easier to find, *KuaiJi* use scope `invalid.illegal` to set their background to red.  
To use the style of *KuaiJi* syntax, you must change your note file's extension name to `.kj`.


# What is a *title*?
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



# How to use *KuaiJi*?
Open a file named `*.kj`, which contain *title*s in it.  
Use **AnXu => Kuaiji Find** menu or `alt+m` shortcut to invoke the *quick panel*.  
Then click one of the *title*s shown in the *quick panel*, current *view* will scroll to make the chosen *title* in the center of the *view port*


# Customization
The command binded to **AnXu => Kuaiji Find** menu and `alt+m` shortcut is `kuaiji_find`,
 or in *camel mode* `KuaijiFind`.  
You can use it to customize the menu and shortcut.


# Special words
*KuaiJi* use **sublime-syntax** to make the special words in the note files colorful.  
The special words include but not limited to:  
Key words of language *C*, e.g. `if else char int float` etc;  
Key words of script *Python*, e.g. `self list dict tuple set bytes bytearray` etc;  
Key words of other program languages;  
Other special words like language names, e.g. `XML HTML YAML Python Json JS ` etc.
