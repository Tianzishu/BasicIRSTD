import zipfile
import shutil
import os


def copy_files(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isfile(s):
            shutil.copy2(s, d)
# 压缩指定文件夹
def zipdir(path, ziph):
    # 循环遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(path):
        for file in files:
            # 将每个文件添加到zip文件中
            ziph.write(os.path.join(root, file))

# 将指定文件夹保存为zip文件
def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w') as zipObj:
        # 添加文件夹及其内容到zip文件中
        zipdir(folder_path, zipObj)

if __name__ == '__main__':
    # 将'test_folder'文件夹压缩为'test_folder.zip'文件
    #copy_files('DCANet', 'mask')
    zip_folder('mask', 'submission.zip')
