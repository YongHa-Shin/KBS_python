from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["numpy", "pandas", "sys"], excludes = [])

exe = [Executable("main.py")]

setup(
    name = 'MXF_Video_renaming_Software',
    version = '1.1',
    author = '신용하',
    description = 'help ingest work',
    options = dict(build_exe = buildOptions),
    executables = exe
)