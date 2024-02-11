import zipfile
import os


def backupToZip(folder):
    # 确保文件夹的路径是绝对路径
    folder = os.path.abspath(folder)

    # 找出此代码应使用的文件名
    # 哪些文件已存在。
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # 创建 ZIP 文件
    print(f"Creating {zipFilename}...")

    backupZip = zipfile.ZipFile(zipFilename, "w")

    # 遍历整个文件夹树并压缩每个文件夹中的文件
    for foldername, subfolders, filenames in os.walk(folder):
        print(f"Adding files in {foldername}...")

        # 使用相对路径添加文件夹中的文件到 ZIP 文件中
        for filename in filenames:
            if filename.startswith(
                os.path.basename(folder) + "_"
            ) and filename.endswith(".zip"):
                continue  # 不备份备份的 ZIP 文件
            backupZip.write(
                os.path.join(foldername, filename),
                arcname=os.path.relpath(os.path.join(foldername, filename), folder),
            )

    backupZip.close()
    print("Done.")


if __name__ == "__main__":
    backupToZip("../backupToZip/")
