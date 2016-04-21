import sys
from cx_Freeze import setup, Executable

setup(
    name='LogoRajzolo',
    version='0.1',
    executables=[Executable("main.py")],
    options={"build_exe": {"packages" : ["pygame", "tkinter"]}}
)