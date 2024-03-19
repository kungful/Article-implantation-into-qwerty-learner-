![图片描述](https://github.com/kungful/Article-implantation-into-qwerty-learner-/blob/main/image2%20-%20%E5%89%AF%E6%9C%AC.png)
![图片描述](https://github.com/kungful/Article-implantation-into-qwerty-learner-/blob/main/image%20-%20%E5%89%AF%E6%9C%AC.png)
使用说明
请搭配这个项目使用 https://github.com/RealKai42/qwerty-learner

翻译后保存到qwerty-learner\public\dicts的目录进行替换，或者如需增加新翻译词典位置模块请到qwerty-learner\src\resources\dictionary.ts进行添加索引。

准备环境：

确保你的电脑上已经安装了Python。
在脚本文件所在目录打开命令行工具（如cmd或PowerShell）。
运行脚本：

双击运行名为 run_script.bat 的批处理文件。
批处理文件会自动检查是否存在虚拟环境，如果不存在，则创建一个名为 myenv 的虚拟环境。
虚拟环境创建完成后，依次安装了 requirements.txt 中所列出的所有依赖项。
安装完成后，自动运行名为 1demo.py 的Python脚本。
替换翻译API：

在 1demo.py 文件中，你可以选择不同的翻译API。当前可选的API有谷歌和必应。
默认使用谷歌翻译API。如果需要切换到必应翻译API，只需修改 1demo.py 中的 api_var.set("谷歌") 为 api_var.set("必应") 即可。
保存翻译结果：

程序会将翻译结果显示在界面上，你可以将结果保存为 JSON 文件。
点击界面上的 “保存” 按钮，选择保存的路径和文件名，即可将翻译结果保存为 JSON 格式的文件。
关闭程序：

当你完成翻译任务后，可以关闭程序界面。
开源协议：

该脚本采用最开放的开源协议 MIT License 进行发布，你可以在遵循许可条款的前提下自由使用、修改和分发。

注意：

为了程序正常运行，请确保网络连接正常，以便于翻译API的调用。
如果遇到任何问题或有疑问，请随时联系作者获取帮助。
