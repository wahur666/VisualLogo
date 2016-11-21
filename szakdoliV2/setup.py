import sys
from cx_Freeze import setup, Executable

setup(
    name='VisualLogo',
    version='1.0',
    description="A visual IDE for logo programming",
    author="Szecsodi Imre",
    executables=[Executable("VisualLogo.py")],
    options={"build_exe": {"packages" : ["pygame", "PIL"]}}
)