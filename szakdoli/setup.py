from cx_Freeze import setup, Executable

setup(
    name='LogoRajzolo',
    version='0.1',
    executables=[Executable("main.py")]
)