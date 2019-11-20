# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:26:05 2019

@author: netel
"""
#加载所需包
import numpy as np
import pandas as pd
import jieba,codecs
#import jieba.posseg as pseg  #标注词性模块
#from pyecharts import Bar,WordCloud

file_ren = "e://working/python/人名.txt"
file_stop = "e://working/python/mystopwords.txt"
file_cut = "e://working/python/平凡的世界1-整段.txt"
file_pos = "e://working/python/平凡的世界1.txt"
file_out = "e://working/python/nameout.txt"

renmings = pd.read_csv(file_ren,engine='python',encoding='utf-8',names=['renming'])['renming']
stopwords = pd.read_csv(file_stop,engine='python',encoding='utf-8',names=['stopword'])['stopword']
#.tolist()
#output = codecs.open(file_out,'w',encoding='utf-8')

book = codecs.open(file_cut,encoding='utf-8')
print('文本读取完毕')
jieba.load_userdict('e://working/python/mydict.txt')

for line in book.readlines():
    words = list(jieba.cut(line))
stopwords1 = [w for w in words if (len(w)==1 and w!=' ')]  #添加停用词
seg = set(words) - set(stopwords) - set(stopwords1) #过滤停用词，得到更为精确的分词
result = [i for i in words if i in seg]
renming = [i.split(' ')[0] for i in set(renmings)] #只要人物名字，出掉词频以及词性
nameswords = [i for i in result if i in set(renming)]  #筛选出人物名字



lineNames = [] #代表list列表数据类型，名字list
 # 每集内人物关系，保存对每一段分词得到当前集中出现的人物名称
 #lineName[i]是一个列表，列表中存储第i段中出现过的人物。
 
with codecs.open(file_pos,'r','utf-8') as f:
    n = 0
    for line in f.readlines(): 
        n+=1
        print('正在处理第{}行'.format(n))
        word = jieba.cut(line)
        lineNames.append([])
        for w in word:#处理名字字典，初始化关系字典
            if w in set(nameswords):
                lineNames[-1].append(w) #如果w在名字集合里面，将w添加到list末尾
                


strnames=[]
for line in lineNames:# 对于每一段 
    if len(line) != 0:
        strnames.append(','.join(line))
    
    
def authors_stat(co_authors_list):
    au_dict = {}  # 单个作者频次统计
    au_group = {}  # 两两作者合作
    for authors in co_authors_list:
        authors = authors.split(',')  # 按照逗号分开每个作者
        authors_co = authors  # 合作者同样构建一个样本
        for au in authors:
            # 统计单个作者出现的频次
            if au not in au_dict:
                au_dict[au] = 1
            else:
                au_dict[au] += 1
            # 统计合作的频次
            authors_co = authors_co[1:]  # 去掉当前作者
            for au_c in authors_co:
                A, B = au, au_c  # 不能用本来的名字，否则会改变au自身
                if A > B:
                    A, B = B, A  # 保持两个作者名字顺序一致
                co_au = A+','+B  # 将两个作者合并起来，依然以逗号隔开
                if co_au not in au_group:
                    au_group[co_au] = 1
                else:
                    au_group[co_au] += 1
    return au_group, au_dict


def generate_matrix(au_group, matrix):
    for key, value in au_group.items():
        A = key.split(',')[0]
        B = key.split(',')[1]
        #Fi = au_dict[A]
        #Fj = au_dict[B]
        #Eij = value*value/(Fi*Fj)
        # 按照作者进行索引，更新矩阵
        if A == B:
            continue
        matrix.loc[A, B] = value
        matrix.loc[B, A] = value
    return matrix


if __name__ == '__main__':
    #co_authors = 'a,b,n,g,d,y//v,b,d,a,s//a,n,d,b,s'
    # co_authors = '张三,里斯,和,sd//和,徐徐,里斯,有,sd//有,和,星,b,sd'
    # co_authors = 'a,b,c//a,c,d//b,c,d'
    #co_authors_list = co_authors.split('//')
    au_group, au_dict = authors_stat(strnames)
    print(au_group)
    print(au_dict)
    au_list = list(au_dict.keys())  # 取出所有单个作者
    # 新建一个空矩阵
    matrix = pd.DataFrame(np.identity(len(au_list)), columns=au_list, index=au_list)
    #print(matrix)
    matrix = generate_matrix(au_group, matrix)
print(matrix)
matrix.to_csv('0412matrix1.csv')
    
'''
with codecs.open('0329node-3.csv', 'w', 'utf-8') as f:
    f.write('Id, Label, Weight\r\n')
    for name, times in names.items():
        f.write(name + ',' + name + ',' + str(times) + '\r\n')

with codecs.open('0329edge-3.csv', 'w', 'utf-8') as f:
    f.write('Source, Target, Weight\r\n')
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                f.write(name + ',' + v + ',' + str(w) + '\r\n')







node = pd.DataFrame(columns=['Id','Label','Weight'])
edge = pd.DataFrame(columns=['Source','Target','Weight'])
for name,times in names.items():  #列表返回键值和值的元组tuple数据，即名字和次数
        node.loc[len(node)] = [name,name,times]
for name,edges in relationships.items():
        for v, w in edges.items():
            if w > 3:
                edge.loc[len(edge)] = [name,v,w]


#nresult = node['Weight'].groupby([node['Id'],node['Label']]).agg({'Weight':np.sum}).sort_values('Weight',ascending = False)
nresult = node['Id','Weight'].groupby([node['Id'],node['Label']]).agg({'Weight':np.sum}).sort_values('Weight',ascending = False)
eresult = edge.sort_values('Weight',ascending = False)
nresult.to_csv('node-new.csv',index = False,encoding='utf-8')
eresult.to_csv('edge-new.csv',index = False,encoding='utf-8')
'''