# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:17:50 2019

@author: netel
"""

#加载所需包
from os import system as s, path as p
from subprocess import getoutput as spgop
import numpy as np
import pandas as pd
import jieba,codecs
import jieba.posseg as pseg  #标注词性模块
from pyecharts import Bar,WordCloud

file_ren = "d://working/python/人名.txt"
file_stop = "d://working/python/mystopwords.txt"
file_cut = "d://working/python/平凡的世界3-整段.txt"
file_out = "d://working/python/nameout.txt"





#导入人名、停用词、特定词库
renmings = pd.read_csv(file_ren,engine='python',encoding='utf-8',names=['renming'])['renming']
stopwords = pd.read_csv(file_stop,engine='python',encoding='utf-8',names=['stopword'])['stopword']
#.tolist()
output = codecs.open(file_out,'w',encoding='utf-8')
book = codecs.open(file_cut,encoding='utf-8')
print('文本读取完毕')
jieba.load_userdict('d://working/python/mydict.txt')

#定义一个分词函数
#def words_cut(book):
#words = list(book)
#bookwords = [w for w in words if w!=' ']
for line in book.readlines():
    words = list(jieba.cut(line))
stopwords1 = [w for w in words if (len(w)==1 and w!=' ')]  #添加停用词

seg = set(words) - set(stopwords) - set(stopwords1) #过滤停用词，得到更为精确的分词
#for w in seg:
#    print(w)
result = [i for i in words if i in seg]
#for w in result:
#    print(w)
#return result

#初次分词
#bookwords = result
renming = [i.split(' ')[0] for i in set(renmings)] #只要人物名字，出掉词频以及词性
nameswords = [i for i in result if i in set(renming)]  #筛选出人物名字
#for w in nameswords:
#    output.write(w)
#统计词频
print('开始统计词频')
bookwords_count = pd.Series(result).value_counts().sort_values(ascending=False)
nameswords_count = pd.Series(nameswords).value_counts().sort_values(ascending=False)
#print(nameswords_count[:30])
#nameswords_count[:30].index

bar = Bar('出现最多的人物TOP20',background_color = 'white',title_pos = 'left',title_text_size = 20)
print('开始画图')
x = nameswords_count[:20].index.tolist()
print('给x')
y = nameswords_count[:20].values.tolist()
print('给y')
bar.add('人物',x, y,xaxis_interval = 0,xaxis_rotate = 30,is_label_show = True)
bar.render(r"e:\03_chart.html")
print('画图输出结束')

#整本小说的词语词云分析
name = nameswords_count.index.tolist()
value = nameswords_count.values.tolist()
wc = WordCloud(background_color = 'white')
wc.add("", name, value, word_size_range=[20, 100],shape='cardioid')
wc.render(r"e:\03_cloud.html")
print('词云输出结束')
