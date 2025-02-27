import pickle as pkl

def mapGroupHunkID2Num(dicts):

    for dict in dicts: # 遍历每个GT

        # 读取 hunkID 列表
        HunkIDs = dict['allHunkID']

        for key in dict:
            # 读取每个group
            if "group" in key:
                # 对该列表进行重映射
                for index in range(len(dict[key])):
                    hunkid = dict[key][index] # 取该列表的每个commitID
                    dict[key][index] = HunkIDs.index(hunkid) # 取HunkIDs对应的index，重写该列表

        # 对hunkID 列表重写
        for index in range(len(HunkIDs)):
            HunkIDs[index] = index

    return dicts

if __name__ == '__main__':
    reponame = 'glide'
    steps = [2, 3, 5]

    for step in steps:
        # 打开所有目录
        with open(r'./dataset/'+reponame+'/HunkIDdict/HunkIDdict_' + str(step) + '.pkl', 'rb') as f:
            HunkID_dict = pkl.load(f)

        newDict = mapGroupHunkID2Num(HunkID_dict)
        with open(r'./dataset/'+reponame+'/HunkIDdict/NewHunkIDdict_' + str(step) + '.pkl', 'wb') as f:
            pkl.dump(newDict, f)

        # print()