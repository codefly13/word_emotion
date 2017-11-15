# coding=utf-8
# -*- coding: cp936 -*-
import jieba
import jieba.posseg as pseg
import codecs
import re
import os
import time
import string
from nltk.probability import FreqDist
open=codecs.open


def split_word(table, content_col):
    word_split_result=[]
    word_class_result=[]
    cnt = 0
    for idx in table.index:
        content = table.ix[idx, content_col]
    #     words = pseg.cut(string) #进行分词
        seg_list = pseg.cut(content) #进行分词
    #     seg_list = jieba.cut(content, cut_all=True)
        a_word_list = []
        a_word_class_list = []
        for w in seg_list:
            if w.word != "":
                a_word_list.append(w.word)       
                a_word_class_list.append(w.flag)
        if len(a_word_list) != len(a_word_class_list) and cnt < 10:
            print(a_word_list)
            print(a_word_class_list)
            cnt+=1
        word_split_result.append("/*/".join(a_word_list))
        word_class_result.append("/*/".join(a_word_class_list))
    return word_split_result, word_class_result


def find_cW_eW(word_split_result, word_class_result):
    word_class_all_record = []
    center_word_all_record = []
    for i in range(len(word_split_result)):
        word_dict={}
        center_words = []
        emotions = []
        a_word_list = word_split_result[i].split("/*/")
        a_word_class_list = word_class_result[i].split("/*/")
        canSelect = 0 # canSelect == 2 表示名词后跟着形容词，可以作为中心词
        a_center_word=None
        a_emotion_word=None
        for j in range(len(a_word_list)):
            a_word = a_word_list[j]
            a_word_class = a_word_class_list[j]
            if "n" in a_word_class and canSelect == 0:
                canSelect=1
                a_center_word=a_word

            if "a" in a_word_class and canSelect == 1:
                canSelect=2
                a_emotion_word = a_word

            if canSelect==2:
                word_dict[a_center_word] = a_emotion_word
                # center_words.append(a_center_word)
                # emotions.append(a_emotion_word)
                canSelect=0

        for key in word_dict:
            center_words.append(key)
            emotions.append(word_dict[key])
                
        center_word_all_record.append("/*/".join(center_words))
        word_class_all_record.append("/*/".join(emotions))
    return center_word_all_record, word_class_all_record

def find_emotion(word_class_all_record, anls_word_table):
    sentiment_anls = []
    for i in range(len(word_class_all_record)):
        a_word_list=[]
        a_anls_list=[]
        a_record = word_class_all_record[i].split("/*/")
        for j in range(len(a_record)):
            aword = a_record[j]
            if aword in anls_word_table.index:
                if anls_word_table.ix[aword, "负面情感词语（中文）"] == 1:
                    a_anls_list.append("-1")
                elif anls_word_table.ix[aword, "正面情感词语（中文）"] == 1:
                    a_anls_list.append("1")
                elif anls_word_table.ix[aword, "中性情感词语（中文）"] == 1:
                    a_anls_list.append("0")
            elif aword!="":
                a_anls_list.append("1")
            else:
                a_anls_list.append("")
                
        if i<5:
            print(a_record)
            print(a_anls_list)
        if len(a_anls_list)!=0:
            sentiment_anls.append("/*/".join(a_anls_list))
        else:
            sentiment_anls.append("")
    return sentiment_anls

