# UseChatGPT
记录ChatGPT的使用，如e用接口，exe封装，有价值的回答等

## 如何将python文件打包成exe程序

Python文件可以使用Pyinstaller等工具将其编译成exe程序。以下是使用Pyinstaller的步骤：

1. 安装Pyinstaller：可在终端中使用pip install pyinstaller命令进行安装。

2. 打开终端并导航到Python文件所在目录。

3. 在终端中使用以下命令将Python文件编译成exe程序：

   ```
   pyinstaller --onefile yourscript.py
   ```

   上述命令将生成一个单文件的exe程序。

4. 编译完成后，在dist文件夹下可以找到生成的exe程序。

注意事项：

- 如果Python文件中有依赖包，则需要在编译时添加参数。例如：

  ```
  pyinstaller --onefile --hidden-import=pandas yourscript.py
  ```

- 编译时需要特别注意Python文件中的路径设置，需要使用绝对路径而不是相对路径，否则可能导致生成的exe程序无法正常运行。

 使用 PyInstaller 打包应用程序时，需要添加 `--add-data` 参数来指定需要打包的文件。例如，可以使用以下命令打包应用程序：

   ```bash
   pyinstaller --add-data="images/*.png:images" main.py
   ```

   上面的命令将会将 `images` 文件夹下的所有 `.png` 图片文件打包进可执行文件中。

使用python3.10
pyinstaller --onefile --add-binary="picture;picture"  --hidden-import=openai --hidden-import=Pillow  ai.py
pyinstaller --onefile --icon=icon.ico  --hidden-import=openai --hidden-import=Pillow  ai.py