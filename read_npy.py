import numpy as np

step = 3
reponame = 'glide'
# input
Adjs = np.load('./Adjset/'+reponame+'/Adj/Adjs_' + str(step) + '.npy', allow_pickle=True)
HunkAdjs = np.load('./Adjset/'+reponame+'/Adj/HunkAdjs_' + str(step) + '.npy', allow_pickle=True)

PAdjs = np.load('./Adjset/'+reponame+'/Padding_Adjs/PAdjs_' + str(step) + '.npy', allow_pickle=True)
PHunkAdjs = np.load('./Adjset/'+reponame+'/Padding_Adjs/PHunkAdjs_' + str(step) + '.npy', allow_pickle=True)

CAdjs = np.load('./Adjset/'+reponame+'/Cutting_Adjs/CAdjs_' + str(step) + '.npy', allow_pickle=True)
CHunkAdjs = np.load('./Adjset/'+reponame+'/Cutting_Adjs/CHunkAdjs_' + str(step) + '.npy', allow_pickle=True)

print('done')


