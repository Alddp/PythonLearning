from pathlib import Path
from zipfile import ZipFile


def backup_to_zip(folder: Path):
    # 根据已存在的文件确定此代码应使用的文件名
    number = 1
    while True:
        zip_filename = folder.name + "_" + str(number) + ".zip"
        if not Path(zip_filename).exists():
            break
        number += 1

    # 创建 ZIP 文件
    print(f"Creating {zip_filename}...")
    with ZipFile(zip_filename, "w") as backup_zip:
        for item in folder.rglob("*"):
            if item.name.startswith(folder.name + "_") and item.name.endswith(".zip"):
                continue  # 不备份备份ZIP文件
            backup_zip.write(str(item))
    print("Done.")


backup_to_zip(Path("D:/Destok/MyGit/PythonLearning/组织文件/myfolder"))
