import pandas as pd
import jieba,codecs
from pyecharts.charts import Bar,WordCloud

def cutWord(file_cut,file_result):
    file_stop = "/Users/aojie654/tmp/python/stopword.txt"
    # file_stop = "E://pythonProjects/mooc/mystopwords.txt"
    stopwords = pd.read_csv(file_stop,engine='python',encoding='utf-8',names=['stopword'])['stopword']
    #source = codecs.open(file_cut,encoding='utf-8')
    source = codecs.open(file_cut, encoding='utf-8')
    result = open(file_result,'w',encoding='utf-8')
    jieba.load_userdict("/Users/aojie654/tmp/sja/text/中篇/白朗/dict.txt")
    #print('文本读取完毕')
    for line in source.readlines():
        words = list(jieba.cut(line))
    stopwords1 = [w for w in words if (len(w) == 1 and w != ' ')]
    seg = set(words) - set(stopwords) - set(stopwords1)
    result_data = [i for i in words if i in seg]
    for i in range(len(result_data)):
        s=str(result_data[i])+" ".replace("'",'')
        result.write(s)
    source.close()
    result.close()
    return result_data

def wordNum(result,filename):#'synthesisDiscussAreaTitleWordNum.txt'
    bookwords_count = pd.Series(result).value_counts().sort_values(ascending=False)
    file = open(filename, 'a', encoding='utf-8')
    for i in range(len(bookwords_count.index)):
        file.write(str(bookwords_count.index[i])+'\t'+str(bookwords_count.values[i])+'\n')
    file.close()
    return bookwords_count

def paint(bookwords_count,filename):
    # 绘图
    bar = Bar('出现最多的词TOP30')
    # bar = Bar('出现最多的词TOP30', background_color='white', title_pos='left', title_text_size=30)
    print('开始画图')
    x = bookwords_count[:30].index.tolist()
    print('给x')
    y = bookwords_count[:30].values.tolist()
    print('给y')
    bar.add('词语', x, y, xaxis_interval=0, xaxis_rotate=30, is_label_show=True)
    bar.render(filename)
    print('画图输出结束')

def wordClound(bookwords_count,filename):
    name = bookwords_count.index.tolist()
    value = bookwords_count.values.tolist()
    wc = WordCloud(background_color='white')
    wc.add("", name, value, word_size_range=[10, 100], shape='cardioid')
    wc.render(filename)
    print('词云输出结束')

if __name__=='__main__':
    #cutWord("E://pythonProjects/mooc/synthesisDicussAreaContentDemo.txt","E://pythonProjects/mooc/synthesisDicussAreaContentCutDemo.txt")


    STresult=cutWord("/Users/aojie654/tmp/sja/text/中篇/白朗/白朗_04_whole.txt","/Users/aojie654/tmp/sja/text/中篇/白朗/白朗_04_whole_AreaTitleCut.txt")
    STbookwords_count = wordNum(STresult,"/Users/aojie654/tmp/sja/text/中篇/白朗/白朗_04_whole_Num.txt")
    paint(STbookwords_count,"/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDicussAreaTitle_chart.html")
    wordClound(STbookwords_count,"/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDicussAreaTitle_wordClound.html")

    # SCresult = cutWord("/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDicussAreaContent.txt", "/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDicussAreaContentCut.txt")
    # SCbookwords_count = wordNum(SCresult,"/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDiscussAreaContentWordNum.txt")
    # paint(SCbookwords_count, "/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDicussAreaContent_chart.html")
    # wordClound(SCbookwords_count, "/Users/aojie654/tmp/sja/text/中篇/白朗/synthesisDicussAreaContent_wordClound.html")

    # CTresult = cutWord("/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaTitle.txt","/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaTitleCut.txt")
    # CTbookwords_count = wordNum(CTresult,"/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaTitleWordNum.txt")
    # paint(CTbookwords_count, "/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaTitle_chart.html")
    # wordClound(CTbookwords_count, "/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicatuonAreaTitle_wordClound.html")

    # CCresult = cutWord("/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaContent.txt", "/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaContentCut.txt")
    # CCbookwords_count = wordNum(CCresult,"/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaContentWordNum.txt")
    # paint(CCbookwords_count, "/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicationAreaContent_chart.html")
    # wordClound(CCbookwords_count, "/Users/aojie654/tmp/sja/text/中篇/白朗/classCommunicatuonAreaContent_wordClound.html")

    # TTresult = cutWord("/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaTitle.txt", "/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaTitleCut.txt")
    # TTbookwords_count = wordNum(TTresult,"/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaTitleWordNum.txt")
    # paint(TTbookwords_count, r"/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaTitle_chart.html")
    # wordClound(TTbookwords_count, r"/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaTitle_wordClound.html")

    # TCresult = cutWord("/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaContent.txt","/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaContentCut.txt")
    # TCbookwords_count = wordNum(TCresult,"/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaContentWordNum.txt")
    # paint(TCbookwords_count, r"/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaContent_chart.html")
    # wordClound(TCbookwords_count, r"/Users/aojie654/tmp/sja/text/中篇/白朗/teacherAnsweringAreaContent_wordClound.html")




    '''
       lines = source.readlines()
       for line in lines:
           words = list(jieba.cut(line))
           stopwords1 = [w for w in words if (len(w) == 1 and w != ' ')]
           seg = set(words) - set(stopwords) - set(stopwords1)
           result_data = [i for i in words if i in seg]
           for i in range(len(result_data)):
               s = str(result_data[i])+" ".replace("'",'')
               result.write(s)
           bookwords_count = pd.Series(result_data).value_counts().sort_values(ascending=False)
           file = open("E://pythonProjects/mooc/synthesisDiscussAreaContentWordNum.txt", 'a', encoding='utf-8')
           for i in range(len(bookwords_count.index)):
               file.write(str(bookwords_count.index[i]) + '\t' + str(bookwords_count.values[i]) + '\n')
           file.close()
           '''
    '''
    bar = Bar('出现最多的词TOP30', background_color='white', title_pos='left', title_text_size=30)
    print('开始画图')
    x = bookwords_count[:30].index.tolist()
    print('给x')
    y = bookwords_count[:30].values.tolist()
    print('给y')
    bar.add('词语', x, y, xaxis_interval=0, xaxis_rotate=30, is_label_show=True)
    bar.render("E:\pythonProjects\mooc\synthesisDicussAreaContent_chart.html")
    print('画图输出结束')

    name = bookwords_count.index.tolist()
    value = bookwords_count.values.tolist()
    wc = WordCloud(background_color='white')
    wc.add("", name, value, word_size_range=[10, 100], shape='cardioid')
    wc.render("E:\pythonProjects\mooc\synthesisDicussAreaContent_wordClound.html")
    print('词云输出结束')
    '''