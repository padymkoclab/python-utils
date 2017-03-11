
import sys
import os
import shutil
import pkgutil
import importlib
import collections
import tkinter


def get_screen_dimensions():
    """Return screen dimension."""

    tk = tkinter.Tk()
    return dict(
        width=tk.winfo_screenwidth(),
        height=tk.winfo_screenheight()
    )


def get_cpu_by_process():
    """Return CPU usage process or a whole system."""

    return 1


def memory_usage_by_process():
    """
    https://pypi.python.org/pypi/memory_profiler
    http://stackoverflow.com/questions/110259/which-python-memory-profiler-is-recommended

    module "resource" - only for UNix

    """


def chart_total_memory_usage():
    """
    Return chart
    Use matlotlib
    """



def print_info_availabled_modules():

    # name this file (module)
    this_module_name = os.path.basename(__file__).rsplit('.')[0]

    # dict for loaders with their modules
    loaders = collections.OrderedDict()

    # names`s of build-in modules
    for module_name in sys.builtin_module_names:

        # find an information about a module by name
        module = importlib.util.find_spec(module_name)

        # add a key about a loader in the dict, if not exists yet
        if module.loader not in loaders:
            loaders[module.loader] = []

        # add a name and a location about imported module in the dict
        loaders[module.loader].append((module.name, module.origin))

    # all available non-build-in modules
    for module_name in pkgutil.iter_modules():

        # ignore this module
        if this_module_name == module_name[1]:
            continue

        # find an information about a module by name
        module = importlib.util.find_spec(module_name[1])

        # add a key about a loader in the dict, if not exists yet
        loader = type(module.loader)
        if loader not in loaders:
            loaders[loader] = []

        # add a name and a location about imported module in the dict
        loaders[loader].append((module.name, module.origin))

    # pretty print
    line = '-' * shutil.get_terminal_size().columns
    for loader, modules in loaders.items():
        print('{0}\n{1}: {2}\n{0}'.format(line, len(modules), loader))
        for module in modules:
            print('{0:30} | {1}'.format(module[0], module[1]))
