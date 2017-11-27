import sys
import jieba
from os import path
from collections import Counter
import jieba.posseg as pseg

d = path.dirname(__file__)

def jiebaclearText(text):
    """
    功能：
       1. 获得文本
       2. 过滤
    """
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(path.join(d, stop_words_path))
    try:
        stop_words = f_stop.read()
    finally:
        f_stop.close()
    stop_words = stop_words.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in stop_words) and len(myword.strip())>1:
            mywordlist.append(myword)
    return mywordlist

def jiebaType(text):
    """
    功能（调试中）：
       1. 获得文本词性分组
       2. 获得停用词性分组
       3. 过滤分组
    """
    mywordlist = []
    stopwordlist = []
    # 得到文本词性分组
    seg_list = pseg.cut(text)
    for i in seg_list:
        mywordlist.append((i.word, i.flag))
    f_stop = open(path.join(d, stop_words_path))
    try:
        stop_words = f_stop.read()
    finally:
        f_stop.close()
    # 得到停用词磁性分组
    stop_words = pseg.cut(text) 
    for s in stop_words:
        stopwordlist.append((s.word, s.flag))
    # 过滤
    filter_list = []
    for each in mywordlist:
        if each in stopwordlist:
            continue
        filter_list.append(each)
    return filter_list

# 路径
stop_words_path = 'stop_words.txt' #停用词可能需要专门定制
text_path = 'child_abuse.txt' 
text = open(path.join(d, text_path)).read()

purged_text = jiebaclearText(text)
# # 直接统计词频
c = str(Counter(purged_text).most_common(20))
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write(c)


    
