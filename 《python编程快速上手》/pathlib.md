**Pathlib 模块使用教程**

**1. 获取路径：**
- 获取当前工作目录: `Path.cwd()`
- 获取用户 home 目录: `Path.home()`
- 获取当前文件路径: `Path(__file__)`
- 根据字符串获取路径: `Path('subdir/demo_02.py')`
- 获取绝对路径: `file.resolve()`

**2. 获取路径组成部分：**
- 文件名（含后缀）: `file.name`
- 文件名（不含后缀）: `file.stem`
- 后缀: `file.suffix`
- 父级目录: `file.parent`
- 锚 (目录前面的部分): `file.anchor`

**3. 子路径扫描：**
- 扫描某个目录下的所有路径: `dir_path.iterdir()`
- 使用模式匹配匹配指定的路径: `cwd.glob('*.txt')` 或 `cwd.rglob('*.txt')`
- 检查路径是否符合规则: `file.match('*.txt')`

**4. 路径拼接：**
- 使用 `/` 或 `joinpath` 拼接路径: `Path.home() / 'dir' / 'file.txt'` 或 `Path.home().joinpath('dir', 'file.txt')`

**5. 路径测试：**
- 判断是否为文件: `Path("archive/demo.txt").is_file()`
- 判断是否为文件夹: `Path("archive/demo.txt").is_dir()`
- 判断路径是否存在: `Path("archive/demo.txt").exists`

**6. 文件操作：**
- 创建文件: `file.touch(exist_ok=True)`
- 创建目录: `path.mkdir(parents=True)`
- 删除目录: `path.rmdir()`
- 删除文件: `path.unlink()`
- 打开文件: `with file.open() as f: print(f.read())`
- 读写文件: `file_path.read_text()`, `file_path.write_text('new words')`
- 移动文件: `txt_path.replace('new_demo.txt')`
- 重命名文件: `new_file = txt_path.with_name('new.txt')`
- 修改后缀名: `new_file = txt_path.with_suffix('.json')`

注意: `pathlib` 模块的面向对象的设计方式，使得路径操作变得更加直观和简单。它不仅提供了对路径的基础操作，还提供了一些高级功能，如路径的迭代、文件的读写等。在 Python 3.6 以上版本，推荐使用 `pathlib` 来处理文件路径。