# 将 entity 图 的 index 文件构成 adj
import pickle
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

def build_graph(vertexlist, sourceList, targetList):
    Graph = nx.DiGraph() # 创建空的有向图

    # 原dataset中的标号都-1，从0开始编号
    for index in range(len(vertexlist)): # 添加结点，0开始编号
        Graph.add_node(vertexlist[index]-1)

    for index in range(len(sourceList)): # 添加边，0开始编号
        Graph.add_edge(sourceList[index]-1, targetList[index]-1)

    return Graph

def build_Adjs(VertexPathList,VertexTypePathList,VertexTypeDict):
    Adjs = [] # 用来存所有图的adj

    for index in range(0, len(VertexPathList)-2, 3): #遍历每个图,for循环控制步长是3

        # 根据路径，分别打开索引文件
        Id_txt = open(VertexPathList[index])
        Source_txt = open(VertexPathList[index+1])
        Target_txt = open(VertexPathList[index+2])
        Type_txt = open(VertexTypePathList[index//3])

        # 分别按行读取
        IdLines = Id_txt.readlines()
        SourceLines = Source_txt.readlines()
        TargetLines = Target_txt.readlines()
        TypeLines = Type_txt.readlines()

        # 分别存入列表
        idList = []
        soureList = []
        targetList = []
        typeList = []

        for index in range(len(IdLines)):
            idList.append(float(IdLines[index].strip()))
            typeList.append(TypeLines[index].strip())

        for index in range(len(SourceLines)):
            soureList.append(float(SourceLines[index].strip()))
            targetList.append(float(TargetLines[index].strip()))

        if len(idList) !=0: # 有的commit是空的，没记录下来，需要删掉该文件
            # 构图
            graph = build_graph(idList, soureList, targetList)

            # # 可视化图
            # fig, ax = plt.subplots()
            # nx.draw(graph, ax=ax, with_labels=False)
            # plt.show()
            # plt.pause(6)  # 间隔的秒数：6s
            # plt.close(fig)

            # get adjs
            Adj = np.array(nx.adjacency_matrix(graph).todense(), dtype=float)

            # add diagonal
            # 获取主对角线元素的索引
            row, col = np.diag_indices_from(Adj)

            # adj的对角线放入节点属性
            # 注意，是按照节点类型分配属性，而不是节点编号
            # 所以不同编号的节点可能有相同的节点属性
            nodeAttributeList = []
            rowlist = list(row)
            for item in rowlist:
                key = typeList[item] # 根据节点编号，查询节点的type
                value = VertexTypeDict[key] # 根据节点的type，查询节点的attribute
                nodeAttributeList.append(value)

            Adj[row,col] = nodeAttributeList # Adj[列表] = 列表

            Adjs.append(Adj) # 顺序append
        else:
            print('Empty commit:', VertexPathList[index])

    return Adjs


if __name__ == '__main__':
    reponame = 'glide'
    steps = [2, 3, 5]

    for step in steps:
        # 打开所有目录
        with open(r'./dataset/'+reponame+'/VertexPathList/VertexPathList_' + str(step) + '.pkl', 'rb') as f:
            VertexPathList = pickle.load(f)

        with open(r'./dataset/'+reponame+'/VertexTypePathList/VertexTypePathList_' + str(step) + '.pkl', 'rb') as f:
            VertexTypePathList = pickle.load(f)

        with open(r'./dataset/'+reponame+'/VertexTypeDict/VertexTypeDict_' + str(step) + '.pkl', 'rb') as f:
            VertexTypeDict = pickle.load(f)

        # 创建所有图的 adjs
        Adjs = build_Adjs(VertexPathList, VertexTypePathList, VertexTypeDict)

        # 定义文件路径
        filepath = r'./Adjset/'+reponame+'/Adj/Adjs_' + str(step) + '.npy'

        # 检查并创建目录
        directory = os.path.dirname(filepath)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 现在尝试写入文件
        try:
            with open(filepath, 'wb') as f:
                np.save(filepath, Adjs) # 每个图的size不一致，无法使用np.array()将列表转换成数组
            print("File saved successfully.")
        except FileNotFoundError:
            print("Directory creation failed. Please check permissions and path.")
        except Exception as e:
            print(f"An error occurred: {e}")



