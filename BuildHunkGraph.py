# 将 hunk 图 的 index 文件构成 adj
import pickle as pkl
import networkx as nx
import numpy as np
import itertools
import os
import matplotlib.pyplot as plt

# buildgraph 中已经删掉了空节点的复合commit，这里不需要再做判别
def build_Adjs(dicts):
    Adjs = [] # 用来存所有图的adj

    # 遍历每个GT, 构图
    for dict in dicts:
        Graph = nx.Graph()  # 创建空的无向图

        # 读取每个GT的hunkID 列表、图中添加节点
        HunkIDs = dict['allHunkID']
        for item in HunkIDs:
            Graph.add_node(item)

        # 读取每个GT的group列表、图中添加边
        for key in dict:
            if "group" in key:
                sourceList = dict[key]
                # 加边
                edges = list(itertools.product(sourceList, sourceList))
                for item in edges:  # 添加边，0开始编号
                    Graph.add_edge(item[0],item[1]) # 这里应该是全连接

        # # 可视化
        # fig, ax = plt.subplots()
        # nx.draw(Graph, ax=ax, with_labels=True)
        # plt.show()

        # 每个GT的adj
        adj = np.array(nx.adjacency_matrix(Graph).todense(), dtype=float)
        # 去掉对角线(去掉hunk的自连边)
        Adj = adj - np.eye(adj.shape[0])

        Adjs.append(Adj)

    return Adjs


if __name__ == '__main__':
    reponame = 'glide'
    steps = [2, 3, 5]
    for step in steps:
        # 打开所有目录
        with open(r'./dataset/'+ reponame +'/HunkIDdict/NewHunkIDdict_' + str(step) + '.pkl', 'rb') as f:
            HunkIDdict = pkl.load(f)

        # 创建所有图的 adjs
        HunkAdjs = build_Adjs(HunkIDdict)

        # 定义文件路径
        filepath = r'./Adjset/'+reponame+'/Adj/HunkAdjs_' + str(step) + '.npy'

        # 检查并创建目录
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 现在尝试写入文件
        try:
            with open(filepath, 'wb') as f:
                np.save(filepath, HunkAdjs) # 每个图的size不一致，无法使用np.array()将列表转换成数组
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")




