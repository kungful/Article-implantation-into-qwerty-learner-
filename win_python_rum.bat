@echo off
REM 检查是否存在虚拟环境，如果不存在则创建
if not exist .\myenv\Scripts\activate.bat (
    python -m venv myenv
)

REM 激活虚拟环境
call .\myenv\Scripts\activate

REM 安装 requirements.txt 中列出的依赖项
pip install -r requirements.txt

REM 运行 Python 脚本
python 1demo.py

REM 关闭虚拟环境
deactivate
