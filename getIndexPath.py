import pickle
import os
from getPath import get_filelist, filter

# 假设 get_filelist 和 filter 函数已经在其他地方定义过了

if __name__ == '__main__':
    reponame = 'glide'
    steps = [2, 3, 5]
    for step in steps:
        dataset_path = '.\\dataset\\' + reponame + '\\' + str(step)
        key_words = ['Index']

        # 获取源文件和目标内容
        filelist = get_filelist(dataset_path, [])
        newfilelist = filter(filelist, [], kw=key_words)

        # 定义文件路径
        filepath = r'./dataset/' + reponame + '/IndexPathList/IndexPathList_' + str(step) + '.pkl'

        # 检查并创建目录
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 现在尝试写入文件
        try:
            with open(filepath, 'wb') as f:
                pickle.dump(newfilelist, f)
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")