
import tkinter
import subprocess


def is_installed(name):
    """Check up if programm is installed in unix-like system."""

    subprocess.check_call


def get_screen_dimensions():

    tk = tkinter.Tk()
    return dict(
        width=tk.winfo_screenwidth(),
        height=tk.winfo_screenheight()
    )
