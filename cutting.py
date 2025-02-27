import numpy as np
import os

# 注意替换项目名称！！！
reponame = 'glide'
steps = [2, 3, 5]

for step in steps:
    dir = './Adjset/'+ reponame +'/Padding_Adjs/PAdjs_' + str(step) + '.npy'

    # 或者叫 truncate
    if os.path.exists(dir):
        PAdjs = np.load('./Adjset/'+ reponame +'/Padding_Adjs/PAdjs_' + str(step) + '.npy', allow_pickle=True)
        PHunkAdjs = np.load('./Adjset/'+ reponame +'/Padding_Adjs/PHunkAdjs_' + str(step) + '.npy', allow_pickle=True)

        if step == 2:
            CAdjs = PAdjs[0:, 0:250, 0:250]
            CHunkAdjs = PHunkAdjs[0:, 0:150, 0:150]

        elif step == 3:
            CAdjs = PAdjs[0:, 0:250, 0:250]
            CHunkAdjs = PHunkAdjs[0:, 0:150, 0:150]

        elif step == 5:
            CAdjs = PAdjs[0:, 0:250, 0:250]
            CHunkAdjs = PHunkAdjs[0:, 0:150, 0:150]

        # 定义文件路径
        CAdjs_path = r'./Adjset/'+ reponame +'/Cutting_Adjs/CAdjs_' + str(step) + '.npy'
        CHunkAdjs_path = './Adjset/'+ reponame +'/Cutting_Adjs/CHunkAdjs_' + str(step) + '.npy'

        # 检查并创建目录
        directory = os.path.dirname(CAdjs_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        directory2 = os.path.dirname(CHunkAdjs_path)
        if not os.path.exists(directory2):
            os.makedirs(directory2)

        # 现在尝试写入文件
        try:
            with open(CAdjs_path, 'wb') as f:
                np.save(CAdjs_path, CAdjs) # 每个图的size不一致，无法使用np.array()将列表转换成数组
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")

        try:
            with open(CHunkAdjs_path, 'wb') as f:
                np.save(CHunkAdjs_path, CHunkAdjs) # 每个图的size不一致，无法使用np.array()将列表转换成数组
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print('step is error')



