import os
from pathlib import Path
from rich import print


def rename_fig(input_folder_path: Path, rename_id: int) -> None:
    """将某个路径下的文件名批量重命名

    Args:
        input_folder_path (Path): 重命名图片编号的文件夹路径
        rename_id (int): 重命名图片时增加的编号值
    """
    # 获取文件夹中所有文件的列表
    file_list = os.listdir(input_folder_path)
    file_list = list(filter(lambda x: "." in x, file_list))
    file_list  = soretd(file_list, key=lambda x: int(x.split(".")[0]))

    # 遍历文件列表
    for file_name in file_list:
        # 获取文件的完整路径
        file_path = os.path.join(input_folder_path, file_name)

        # 检查文件是否是图片文件（以.jpg或.png结尾）
        if file_name.lower().endswith(('.jpg', '.png')):
            # 解析文件名和扩展名
            name, extension = os.path.splitext(file_name)

            # 将文件编号加100
            new_name = str(int(name) + rename_id)

            # 构建新的文件名
            new_file_name = new_name + extension

            # 构建新的文件路径
            new_file_path = os.path.join(input_folder_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)

    print("🚀🚀🚀 [italic bold green]Code Ending!!!")


if __name__ == '__main__':
    # 指定包含图片的文件夹路径
    folder_path = r'./figure'
    rename_id = 99

    rename_fig(Path(folder_path), rename_id)
