@echo off

REM 获取脚本所在目录
set script_dir=%~dp0

REM 定义虚拟环境目录
set venv_dir=%script_dir%myenv

REM 切换到脚本所在目录
cd /d %script_dir%

REM 检查是否存在虚拟环境
if exist %venv_dir%\Scripts\activate.bat (
    REM 如果存在，则激活虚拟环境并运行脚本
    call %venv_dir%\Scripts\activate
    python %script_dir%1demo.py
    REM 关闭虚拟环境
    deactivate
) else (
    REM 如果不存在，则创建虚拟环境，并运行脚本
    python -m venv %venv_dir%
    call %venv_dir%\Scripts\activate
    pip install -r %script_dir%requirements.txt
    python %script_dir%1demo.py
  
)
