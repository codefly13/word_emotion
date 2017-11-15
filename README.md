# word_emotion
**./train.csv** 训练集
**./test.csv** 测试集
**./hownet** 额外的词典

**./clean_data/**
分析主题缺失率，提取情感词和词性
----- text analysis.ipynb 主文件


**./anls_word_dict_construct.ipynb**
根据hownet文件夹数据和训练数据的情感词和词性扩充词典
输出
----anls_word_dict.csv 词性词典


**./test_v1.ipynb**
读取测试数据，分词和确定词性，获取主题词--情感词对，查询词典确定词性
输出
----result.csv 结果


**./tool.py**
split_word(table, content_col)
分词
输入：
----table， dataframe对象
----content_col， content的字段名
输出：
----word_split_result， 分词结果
----word_class_result， 词性


find_cW_eW(word_split_result, word_class_result)
确定主题和情感词
输入：
----word_split_result， 分词结果
----word_class_result， 词性
输出：
----center_word_all_record， 主题词列表，一个子列表一个记录
----word_class_all_record， 情感词列表，一个子列表一个记录


find_emotion(word_class_all_record, anls_word_table)
查字典确定情感词词性
输入：
----word_class_all_record， 情感词列表
----anls_word_table， 词性字典
输出：
----sentiment_anls， 词性列表，一个子列表一个记录
