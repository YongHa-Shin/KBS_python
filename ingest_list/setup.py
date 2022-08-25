from cx_Freeze import setup, Executable
import sys

buildOptions = dict(packages = ["numpy", "pandas", "sys"], excludes = [])

exe = [Executable("main.py")]

setup(
    name = 'MXF_Video_renaming_Software',
    version = '1.0',
    author = '뉴스시스템개발부 신용하',
    description = 'help ingest work',
    options = dict(build_exe = buildOptions),
    executables = exe
)
