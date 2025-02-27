import numpy as np
import os

if __name__ == '__main__':
    reponame = 'glide'
    steps = [2, 3, 5]

    for step in steps:
        # padding entity graph
        Adjs = np.load('./Adjset/'+ reponame +'/Adj/Adjs_' + str(step) + '.npy', allow_pickle=True)

        rows = []
        for array in Adjs:
            rows.append(array.shape[0])
        max_row = max(rows) # row = col

        PAdjs = []
        for array in Adjs:
            diff = max_row-array.shape[0]
            PAdj = np.pad(array,
                           ((0, diff), # 上下轴，后面填充差值
                            (0, diff)),# 左右轴，后面填充差值
                           'constant')
            PAdjs.append(PAdj)

        # padding hunkID graph
        HunkAdjs = np.load('./Adjset/'+ reponame +'/Adj/HunkAdjs_' + str(step) + '.npy', allow_pickle=True)

        rows1 = []
        for array in HunkAdjs:
            rows1.append(array.shape[0])
        max_row1 = max(rows1) # row = col

        PHunkAdjs = []
        for array in HunkAdjs:
            diff1 = max_row1-array.shape[0]
            PHunkAdj = np.pad(array,
                           ((0, diff1), # 上下轴，后面填充差值
                            (0, diff1)), # 左右轴，后面填充差值
                           'constant')
            PHunkAdjs.append(PHunkAdjs)

        # 定义文件路径
        PAdjs_path = './Adjset/' + reponame + '/Padding_Adjs/PAdjs_' + str(step) + '.npy'
        PHunkAdjs_path = './Adjset/'+ reponame +'/Padding_Adjs/PHunkAdjs_' + str(step) + '.npy'

        # 检查并创建目录
        directory = os.path.dirname(PAdjs_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        directory2 = os.path.dirname(PHunkAdjs_path)
        if not os.path.exists(directory2):
            os.makedirs(directory2)

        # 现在尝试写入文件
        try:
            with open(PAdjs_path, 'wb') as f:
                np.save(PAdjs_path, PAdjs) # 每个图的size不一致，无法使用np.array()将列表转换成数组
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            with open(PHunkAdjs_path, 'wb') as f:
                np.save(PHunkAdjs_path, PHunkAdjs) # 每个图的size不一致，无法使用np.array()将列表转换成数组
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
