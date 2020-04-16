import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Secret Island (debug)",
    version = "0.0.2",
    description = "",
    executables = [Executable("main.py", base = base, icon="icon.ico")]
)