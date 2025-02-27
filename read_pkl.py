import pickle
import numpy as np
step = 2
reponame = 'glide'

# rb是2进制编码文件，文本文件用r
f1 = open(r'./dataset/'+reponame+'/VertexPathList/VertexPathList_' + str(step) + '.pkl','rb')
f2 = open(r'./dataset/'+reponame+'/VertexTypePathList/VertexTypePathList_' + str(step) + '.pkl','rb')
f3 = open(r'./dataset/'+reponame+'/VertexTypeDict/VertexTypeDict_' + str(step) + '.pkl','rb')
f4 = open(r'./dataset/'+reponame+'/GTPathList/GTPathList_' + str(step) + '.pkl','rb')
f5 = open(r'./dataset/'+reponame+'/IndexPathList/IndexPathList_' + str(step) + '.pkl','rb')
f6 = open(r'./dataset/'+reponame+'/HunkIDdict/HunkIDdict_' + str(step) + '.pkl','rb')
f7 = open(r'./dataset/'+reponame+'/HunkIDdict/NewHunkIDdict_' + str(step) + '.pkl','rb')
f8 = open(r'./dataset/'+reponame+'/HunkIDdict/HunkIDmap_' + str(step) + '.pkl','rb')

VertexPathList = pickle.load(f1)
VertexTypePathList = pickle.load(f2)
VertexTypeDict = pickle.load(f3)
GTPathList = pickle.load(f4)
IndexPathList = pickle.load(f5)
HunkIDdict = pickle.load(f6)
NewHunkIDdict = pickle.load(f7)
HunkIDmap = pickle.load(f8)

print(VertexTypePathList)