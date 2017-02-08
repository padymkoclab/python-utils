
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
