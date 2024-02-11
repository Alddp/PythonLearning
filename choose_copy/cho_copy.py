""" 编写一个遍历目录树以查找具有特定扩展名(如 .pdf 或 .jpg)的文件的程序。
    将这些文件复制到新文件夹，无论它们位于何处。"""

from pathlib import Path
import shutil


def find_file(folder: Path, suffix: str, new_path: Path):
    new_path.mkdir(parents=True, exist_ok=True)  # Ensure the new directory exists

    for filename in folder.rglob(f"*.{suffix}"):
        target_filename = new_path / filename.name

        if not target_filename.exists():
            print(filename.parent)
            print(f"copy{filename.name} ---> {target_filename}\n")
            shutil.copy(filename, target_filename)

        else:
            print(f"{target_filename} already exists!")


if __name__ == "__main__":
    # find_file(Path(r"D:\Destok\fruits"), "jpg", Path(r"D:\Destok\fruits\photo"))
    find_file(Path(r"D:\Destok\自律会文件"), "xls", Path(r"D:\Destok\自律会文件\xls"))
