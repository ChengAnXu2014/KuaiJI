import sys
import os
import re
import json
from os import path
import zipfile
import zipimport
import shutil
import time
from textwrap import dedent
from threading import Event, Lock

try:
    str_cls = unicode 
except (NameError):
    str_cls = str
    '''N
    下面用到 str_cls 时会报错'未定义';
    然后会跳转到 try: 语句块；
    如果本解释器支持 unicode ，try: 语句块不会出错，定义 str_cls = unicode;
    如果本解释器不支持 unicode, try: 语句块会报 'NameError';
    跳转到 except (NameError): 语句块, 定义 str_cls = str 。
    Python 3之前，对 unicode 支持不全面，有两种字符串类：str 和 unicode.
    Python 3之后，全面支持 unicode, unicode 类就没用了。
    '''

import sublime

# import 本插件自带的 modules
from . import sys_path
from .console_write import console_write
from .package_disabler import PackageDisabler
from .settings import pc_settings_filename, load_list_setting, save_list_setting


《《Event()》》
class SwapEvent():
    # 初始化时，定义自己的 Event 对象并设 internal flag 为 True
    def __init__(self):
        self._ev = Event()
        self._ev.set()


    def in_process(self):
        return not self._ev.is_set()


    # 设 internal flag 为 False，后续通过 wait() 排队的队列中的下一个线程，会等其执行完毕并重设 internal flag 为 True 时，再开始运行，以此类推
    def start(self):
        self._ev.clear()

    # 设 internal flag 为 True，唤醒之前通过 wait() 暂停的，优先级最高的线程
    def end(self):
        self._ev.set()

    # 调用 wait() 方法进入线程队列，等到 internal flag 为 True 且轮到自己时，开始运行
    def wait(self):
        self._ev.wait()

《《Lock()》》
loader_lock = Lock()
# 只有当loader_lock 通过 acquired 方法被锁定时，才能访问以下变量？？？：//These variables should only be touched while loader_lock is acquired(获得)
swap_event = SwapEvent()
non_local = {
    'loaders': None,
    'last_action': 0.0
}


loader_package_name = u'0_package_control_loader'
# 默认的加载器包名为'0_package_control_loader';
# ST3000版本之前，通过PC安装的插件包以普通目录形式保存；
# ST主版本号和Python保持一致
if sys.version_info < (3,):
    loader_package_path = path.join(sys_path.packages_path, loader_package_name)
    
    # ST3.0版本之后，通过PC安装的插件包以'.sublime-package'形式保存
else:
    loader_package_path = path.join(sys_path.installed_packages_path, u'%s.sublime-package' % loader_package_name)

'''
无法删除ZIP文档中的文件，所以只能把其它文件复制到一个新的ZIP文档中，然后将新文档和原文档名称互换。
'''
new_loader_package_path = loader_package_path + u'-new'
intermediate_loader_package_path = loader_package_path + u'-intermediate'


《《def __update_loaders(z):》》
    """
    更新缓存的 loaders_list,在调用本函数前必须 acquire loader_lock

    :param z:
        The zipfile.ZipFile object to list the files in
    """

    non_local['loaders'] = []
    for filename in z.namelist():
        
        
        # 在Python2中 str 和 bytes(Python 2 所谓的 unicode) 之间会隐晦地自动转换，所以不用手动转换。
        if not isinstance(filename, str_cls):
            
            # 在Python3中，对 str 和 bytes 做了明确区分，且必须手动转换。
            filename = filename.decode('utf-8') # encode	str to bytes;decode		bytes to str
        non_local['loaders'].append(filename)


《《def is_swapping():》》
    """
    If the loader is currently being swapped

    :return:
        Boolean
    """

    loader_lock.acquire()
    swapping = swap_event.in_process()
    loader_lock.release()
    return swapping


《《def exists(name):》》
    """
    If a loader for the specified dependency(依赖) is installed

    :param name:
        The dependency(依赖) to check for a loader for
    """

    return _existing_info(name, False)[0] is not None


《《def _existing_info(name, return_code):》》
    """
    Returns info about loader for the specified dependency(依赖)

    :param name:
        A unicode string of the name of the dependency(依赖) to check for

    :param return_code:
        A boolean, if the loader code should be returned also

    :return:
        A 2-element tuple:
         - [0]: None if loader does not exist, otherwise unicode string of load_order
         - [1]: None if loader does not exist or return_code is False, otherwise a unicode string of loader code
    """

    if not path.exists(loader_package_path):
        return (None, None)

    
    # '(\\d\\d)'子表达式匹配到的内容，后面通过 match.group(1) 被引用
    loader_filename_regex = u'^(\\d\\d)-%s.py$' % re.escape(name)

    load_order = None
    code = None

    if sys.version_info < (3,):
        # ST3版本之前不支持 .sublime-package 包，而是普通文件夹形式。
        for filename in os.listdir(loader_package_path):
            match = re.match(loader_filename_regex, filename)
            if match:
                load_order = match.group(1)
                if return_code:
                    loader_path = os.path.join(loader_package_path, filename)
                    
                    # r		读取；b		二进制
                    with open(loader_path, 'rb') as f:
                        code = f.read().decode('utf-8') # decode	bytes to str
                break
        return (load_order, code)

    # We acquire a lock so that multiple removals don't stomp on each other
    loader_lock.acquire()
《《aaaaa》》
    try:
        
        # if 块更新已有 package，即添加新版，旧版会在其它地方删除
        if swap_event.in_process() and os.path.exists(new_loader_package_path):
            loader_path_to_check = new_loader_package_path
            
            # else 块添加新 package
        else:
            loader_path_to_check = loader_package_path

        # ST3之后采用 .sublime-package 包，为了提高执行效率，会缓存 loaders 列表
        if non_local['loaders'] is None:
            with zipfile.ZipFile(loader_path_to_check, 'r') as z:
                __update_loaders(z)
                # 打开要添加的ZIP文件，返回对应的 zipfile 对象 z;
                # 然后将 z 中所有目录添加到 non_local['loaders']列表中。
《《eeeee》》
        for filename in non_local['loaders']:
            match = re.match(loader_filename_regex, filename)
            if match:
                load_order = match.group(1)
                if return_code:
                    with zipfile.ZipFile(loader_path_to_check, 'r') as z:
                        code = z.read(filename).decode('utf-8')
                break
    except (zipfile.BadZipfile, OSError):
        non_local['loaders'] = []
        return (None, None)

    finally:
        loader_lock.release()

    return (load_order, code)

《《bbbbb》》
def add_or_update(priority, name, code=None):
    """
    Adds a loader if none exists for a package, or replaces an existing one.
    May block while waiting for a loader removal to happen.

    :param priority:
        A two-digit string. If a dep has no dependencies, this can be
        something like '01'. If it does, use something like '10' leaving
        space for other entries

    :param name:
        The name of the dependency(依赖) as a unicode string

    :param code:
        Any special loader code, otherwise the default will be used
    """

    load_order, existing_code = _existing_info(name, True)

    if load_order is not None:
        if not code:
            code = _default_loader(name)

        # Everything is up-to-date
        if load_order == priority and code.strip() == existing_code.strip():
            return

        remove(name)
        swap_event.wait()

    add(priority, name, code)


def add(priority, name, code=None):
    """
    Adds a dependency(依赖) to the loader

    :param priority:
        A two-digit string. If a dep has no dependencies, this can be
        something like '01'. If it does, use something like '10' leaving
        space for other entries

    :param name:
        The name of the dependency(依赖) as a unicode string

    :param code:
        Any special loader code, otherwise the default will be used
    """
《《ccccc》》
    if not code:
        code = _default_loader(name)

    loader_filename = '%s-%s.py' % (priority, name)

    just_created_loader = False

    loader_metadata = {
        "version": "1.0.0",
        "sublime_text": "*",
        # Tie the loader to the platform so we can detect people syncing packages incorrectly.
        "platforms": [sublime.platform()],
        "url": "https://github.com/wbond/package_control/issues",
        "description": "Package Control dependency(依赖) loader"
    }
    loader_metadata_enc = json.dumps(loader_metadata).encode('utf-8') # encode: str to bytes; decode:bytes to str
《《ddddd》》
    if sys.version_info < (3,):
        if not path.exists(loader_package_path):
            just_created_loader = True
            os.mkdir(loader_package_path, 0o755) # u	rwx; g&o	rx; 只适用于linux系统，Windows系统没这种权限
            with open(path.join(loader_package_path, 'dependency(依赖)-metadata.json'), 'wb') as f:
                f.write(loader_metadata_enc)

        loader_path = path.join(loader_package_path, loader_filename)
        
        # b	以二进制模式打开，w	用于写入
        with open(loader_path, 'wb') as f:
            f.write(code.encode('utf-8')) # encode	str to bytes

    else:
        # 确保Python在尝试 import modules 时，不使用旧的 file listing for the loader
        if loader_package_path in zipimport._zip_directory_cache:
            del zipimport._zip_directory_cache[loader_package_path]


            loader_lock.acquire()

            # If a swap of the loader .sublime-package was queued because of a
            # f        try:ile being removed, we need to add the new loader code the the
            # .sublime-package that will be swapped into place shortly.
            if swap_event.in_process() and os.path.exists(new_loader_package_path):
                package_to_update = new_loader_package_path
            else:
                package_to_update = loader_package_path

            mode = 'w'
            just_created_loader = True

            # Only append if the file exists and is a valid zip file
            if os.path.exists(package_to_update):
                # Even if the loader was invalid, it still won't show up as a
                # "new" file via filesystem notifications, so we have to
                # manually load the code.
                just_created_loader = False
                try:
                    with zipfile.ZipFile(package_to_update, 'r') as rz:
                        # Make sure the zip file can be read
                        res = rz.testzip()
                        if res is not None:
                            raise zipfile.BadZipfile('zip test failed')
                        mode = 'a'
                except (zipfile.BadZipfile, OSError):
                    os.unlink(package_to_update)

            with zipfile.ZipFile(package_to_update, mode) as z:
                if mode == 'w':
                    z.writestr('dependency(依赖)-metadata.json', loader_metadata_enc)
                z.writestr(loader_filename, code.encode('utf-8'))
                __update_loaders(z)

        finally:
            loader_lock.release()

        if not just_created_loader and not swap_event.in_process():
            # Manually execute the loader code because Sublime Text does not
            # detect changes to the zip archive, only if the file is new.
            importer = zipimport.zipimporter(loader_package_path)
            importer.load_module(loader_filename[0:-3])

    # Clean things up for people who were tracking the master branch
    if just_created_loader:
        old_loader_sp = path.join(sys_path.installed_packages_path, '0-package_control_loader.sublime-package')
        old_loader_dir = path.join(sys_path.packages_path, '0-package_control_loader')

        removed_old_loader = False

        if path.exists(old_loader_sp):
            removed_old_loader = True
            os.remove(old_loader_sp)

        if path.exists(old_loader_dir):
            removed_old_loader = True
            try:
                shutil.rmtree(old_loader_dir)
            except (OSError):
                open(os.path.join(old_loader_dir, 'package-control.cleanup'), 'w').close()

        if removed_old_loader:
            console_write(
                u'''
                Cleaning up remenants of old loaders
                '''
            )

            pc_settings = sublime.load_settings(pc_settings_filename())
            orig_installed_packages = load_list_setting(pc_settings, 'installed_packages')
            installed_packages = list(orig_installed_packages)

            if '0-package_control_loader' in installed_packages:
                installed_packages.remove('0-package_control_loader')

            for name in ['bz2', 'ssl-linux', 'ssl-windows']:
                dep_dir = path.join(sys_path.packages_path, name)
                if path.exists(dep_dir):
                    try:
                        shutil.rmtree(dep_dir)
                    except (OSError):
                        open(os.path.join(dep_dir, 'package-control.cleanup'), 'w').close()
                if name in installed_packages:
                    installed_packages.remove(name)

            save_list_setting(
                pc_settings,
                pc_settings_filename(),
                'installed_packages',
                installed_packages,
                orig_installed_packages
            )


def remove(name):
    """
    Removes a loader by name

    :param name:
        The name of the dependency(依赖)
    """

    if not path.exists(loader_package_path):
        return

    loader_filename_regex = u'^\\d\\d-%s.pyc?$' % re.escape(name)

    if sys.version_info < (3,):
        for filename in os.listdir(loader_package_path):
            if re.match(loader_filename_regex, filename):
                os.remove(path.join(loader_package_path, filename))
        return

    removed = False

    # We acquire a lock so that multiple removals don't stomp on each other
    loader_lock.acquire()

    try:
        # This means we have a new loader waiting to be installed, so we want
        # the source loader zip to be that new one instead of the original
        if swap_event.in_process() and os.path.exists(new_loader_package_path):
            if os.path.exists(intermediate_loader_package_path):
                os.remove(intermediate_loader_package_path)
            os.rename(new_loader_package_path, intermediate_loader_package_path)
            old_loader_z = zipfile.ZipFile(intermediate_loader_package_path, 'r')

        # Under normal circumstances the source loader zip should be the
        # loader_package_path
        else:
            old_loader_z = zipfile.ZipFile(loader_package_path, 'r')

        new_loader_z = zipfile.ZipFile(new_loader_package_path, 'w')
        for enc_filename in old_loader_z.namelist():
            if not isinstance(enc_filename, str_cls):
                filename = enc_filename.decode('utf-8')
            else:
                filename = enc_filename
            if re.match(loader_filename_regex, filename):
                removed = True
                continue
            new_loader_z.writestr(enc_filename, old_loader_z.read(enc_filename))

        __update_loaders(new_loader_z)

    finally:
        old_loader_z.close()
        new_loader_z.close()
        if os.path.exists(intermediate_loader_package_path):
            os.remove(intermediate_loader_package_path)

    # If we did not remove any files and there isn't already a swap queued, that
    # means that nothing in the zip changed, so we do not need to disable the
    # loader package and then re-enable it
    if not removed and not swap_event.in_process():
        if os.path.exists(new_loader_package_path):
            os.remove(new_loader_package_path)
        loader_lock.release()
        return

    def _do_disable():
        disabler = PackageDisabler()
        disabler.disable_packages(loader_package_name, 'loader')
    sublime.set_timeout(_do_disable, 10)

    # Note: If we "manually" loaded the dependency(依赖) loader before it will not
    # be unloaded automatically when the package is disabled. Since it is
    # highly doubtful that anyone would define `plugin_unloaded` in his
    # `loader.py`, we don't necessarily have to implement it, but this is just
    # a note.

    # It is possible multiple dependencies will be removed in quick succession,
    # however we pause to let the loader file system lock to be released on
    # Windows by Sublime Text. The swap_event variable makes sure we don't have
    # multiple timeouts set to replace the loader zip with the new version, thus
    # hitting a race condition where files are overwritten and rename operations
    # fail because the source file doesn't exist.
    if not swap_event.in_process():
        swap_event.start()
        sublime.set_timeout(_do_swap, 1000)

    non_local['last_action'] = time.time()
    loader_lock.release()


def _do_swap():
    """
    Swap the loader package with the new version
    """

    if not loader_lock.acquire(blocking=False):
        sublime.set_timeout(_do_swap, 500)
        return

    if time.time() - non_local['last_action'] < 0.9:
        sublime.set_timeout(_do_swap, 500)
        loader_lock.release()
        return

    if os.path.exists(loader_package_path) and os.path.exists(new_loader_package_path):
        os.remove(loader_package_path)
        os.rename(new_loader_package_path, loader_package_path)

    sublime.set_timeout(_do_reenable, 500)


def _do_reenable():
    """
    Re-enable the loader package after a swap has been done
    """

    disabler = PackageDisabler()
    disabler.reenable_package(loader_package_name, 'loader')
    swap_event.end()
    loader_lock.release()


def _default_loader(name):
    """
    Generate the default loader code for a dependency(依赖)

    :param name:
        A unicode string of the name of the dependency(依赖)

    :return:
        A unicode string of the Python code to execute to load the dependency(依赖)
    """

    code = """
        from package_control import sys_path
        sys_path.add_dependency(%s)
    """ % repr(name)
    return dedent(code).lstrip()
