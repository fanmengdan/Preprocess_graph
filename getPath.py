import os

# 遍历 文件夹 及其 子文件夹中 的文件，并存储在一个列表中
# 输入: 文件夹路径、空文件列表[]
# 返回: 文件列表Filelist,包含文件名（完整路径）

def get_filelist(dir, Filelist): # path, list
    newDir = dir
    # 顺序遍历文件
    if os.path.isfile(dir):
        Filelist.append(dir)
        # 若只是要返回文件文，使用这个
        # Filelist.append(os.path.basename(dir))

    # 顺序遍历 子文件夹下 的 文件
    elif os.path.isdir(dir):
        # os.listdir(path) 输出路径下所有文件的文件名
        for subDir in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, subDir) # 拼接绝对路径
                get_filelist(newDir, Filelist) # 递归, 递归到n轮才能进入最深的目录

    return Filelist

# 过滤 不是记录端点的 目录item
def filter (Filelist, newfilelist, kw):
    for item in Filelist:
        if any(word if word in item else False for word in kw):
            newfilelist.append(item)
    return newfilelist



