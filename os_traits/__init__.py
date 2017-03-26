#import os
#import glob
#import sys
#
#this_mod = sys.modules.get(__name__)
#this_dir = os.path.dirname(this_mod.__file__)
#print this_dir
#
#for dirname, _, files in os.walk(this_dir):
#    pyfiles = [f for f in files if f.endswith(".py") and not f.startswith("_")]
#    subdir_path = dirname.lstrip(this_dir)
#    rel_path = ".%s" % subdir_path.replace("/", ".")
#    print rel_path, pyfiles
#    if pyfiles:
#        for pyfile in pyfiles:
#            mod_name = pyfile.rstrip(".py")
#            from rel_path import mod_name

import importlib
import pkgutil
import sys


def import_submodules(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        results[full_name] = importlib.import_module(full_name)
        if recursive and is_pkg:
            results.update(import_submodules(full_name))
    return results

this_mod = sys.modules.get(__name__)
import_submodules(this_mod)
