import sys
import os
from os.path import dirname


'''
本文件把 package_control 子目录添加到 sys.path 的第一位；
以便让所有其它 packages 都依靠 PackageControl 来实现公共功能；
如 event helpers, 添加内容到 sys.path, 从网上下载文件等。
'''

if sys.version_info >= (3,):
    def decode(path):
        return path

    def encode(path):
        return path

    loader_dir = dirname(__file__) # __file__是内部变量，代表本文件的fullPath

else:
    def decode(path):
        if not isinstance(path, unicode):
            path = path.decode(sys.getfilesystemencoding()) # 我搞错了，3之前，Python 有unicode对象，3之后没了。可能3之后就全面支持unicode,所以不需要了。
        return path

    def encode(path):
        if isinstance(path, unicode):
            path = path.encode(sys.getfilesystemencoding())
        return path

    loader_dir = decode(os.getcwd())


st_dir = dirname(dirname(loader_dir))

found = False
if sys.version_info >= (3,):
    installed_packages_dir = os.path.join(st_dir, u'Installed Packages')
    pc_package_path = os.path.join(installed_packages_dir, u'Package Control.sublime-package')
    if os.path.exists(encode(pc_package_path)):
        found = True

if not found:
    packages_dir = os.path.join(st_dir, u'Packages')
    pc_package_path = os.path.join(packages_dir, u'Package Control')
    if os.path.exists(encode(pc_package_path)):
        found = True

# Handle the development environment
if not found and sys.version_info >= (3,):
    import Default.sort # 秀啊！！！
    if os.path.basename(Default.sort.__file__) == 'sort.py':
        packages_dir = dirname(dirname(Default.sort.__file__)) # 'Installed Packages'和'Packages'目录都找不到时，直接找系统'Packages'目录
        pc_package_path = os.path.join(packages_dir, u'Package Control')
        if os.path.exists(encode(pc_package_path)):
            found = True

《《if found:》》
    if os.name == 'nt':
        from ctypes import windll, create_unicode_buffer
        buf = create_unicode_buffer(512) # buf是一个ctype 的 c_wchar 数组
        if windll.kernel32.GetShortPathNameW(pc_package_path, buf, len(buf)):
            pc_package_path = buf.value
            # 将pc_package_path转化为简写模式？？？
            # 可能在Windows nt系统下，想把目录添加到 sys.path 必须这样转换，虽然还不懂究竟是什么意思。
            # 被添加到 sys.path 的目录下的文件、包和模块，才能直接 import 。

    sys.path.insert(0, encode(pc_package_path))
    import package_control
    
    # We remove the import path right away so as not to screw up
    # Sublime Text and its import machinery
    sys.path.remove(encode(pc_package_path))

else:
    print(u'Package Control: Error finding main directory from loader')
